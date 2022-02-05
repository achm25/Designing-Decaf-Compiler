
int_size = 4
double_size = 8
string_size = 1
bool_size = 1

TYPE_IS_STRING = "string"
TYPE_IS_INT = "int"
TYPE_IS_DOUBLE = "double"

class CodeGenerator:

    @staticmethod
    def new_variable(symbol_table, variable):
        code = []
        data = []

        #todo why we need new scope?
        #current_scope = symbol_table.new_scope()
        symbol_table.current_scope.add_symbol(variable)



        if variable.v_type.name == TYPE_IS_INT:
            name_generate = symbol_table.current_scope.root_generator()
            name_generate = name_generate + "__" +  variable.identifier.name
            data += [f"{name_generate}: .word 0"]


        size = int_size
        if variable.v_type.name == TYPE_IS_DOUBLE:
            size = 8
            name_generate = symbol_table.current_scope.root_generator()
            name_generate = name_generate + "__" +  variable.identifier.name
            data += [f"{name_generate}: .double 0.0"]

        if variable.v_type.name == TYPE_IS_STRING:
            name_generate = symbol_table.current_scope.root_generator()
            name_generate = name_generate + "__" +  variable.identifier.name
            data += [f"{name_generate}: .asciiz \"NONE\""]


            #todo should be deleted
        if not (variable.is_global or variable.is_in_class or variable.is_func_param):
            variable.local_offset = symbol_table.local_offset
            symbol_table.local_offset += size
            code += [
                f"\tsubu $sp, $sp, {size}\t# Decrement sp to make space for variable {variable.identifier.name}."
            ]

        symbol_table.data_storage += data
        return code

    @staticmethod
    def variable_definition_with_assign(symbol_table, variable):
        code = []
        return code

    @staticmethod
    def variable_definition(symbol_table,variable):
        code  = CodeGenerator.new_variable(symbol_table, variable)
        return code

    @staticmethod
    def new_function(symbol_table, function):
        symbol_table.local_offset = 0
        if function.parent_class is not None:
            function.label = (
                f"{function.parent_class.identifier.name}_{function.identifier.name}"
            )
        curr_scope = symbol_table.new_scope(name=function.identifier.name)
        for param in function.params:
            curr_scope.add_symbol(param)
        code = [
            f"{function.label}:",
            "\tsubu $sp, $sp, 8\t# decrement sp to make space to save ra, fp",
            "\tsw $fp, 8($sp)\t# save fp",
            "\tsw $ra, 4($sp)\t# save ra",
            "\taddiu $fp, $sp, 8\t# set up new fp",
        ]
        code += function.block.cgen(symbol_table)
        code += [
            "\tmove $sp, $fp\t\t# pop callee frame off stack",
            "\tlw $ra, -4($fp)\t# restore saved ra",
            "\tlw $fp, 0($fp)\t# restore saved fp",
            "\tjr $ra\t\t# return from function",
        ]
        # Reset
        symbol_table.local_offset = 0
        symbol_table.current_scope = curr_scope.parent_scope
        return code

    @staticmethod
    def new_void_function(symbol_table, function):
        symbol_table.local_offset = 0
        if function.parent_class is not None:
            function.label = (
                f"{function.parent_class.identifier.name}_{function.identifier.name}"
            )
        curr_scope = symbol_table.new_scope(name=function.identifier.name)
        for param in function.params:
            curr_scope.push_symbol(param)
        code = [
            f"{function.label}:",
            "\tsubu $sp, $sp, 8\t# decrement sp to make space to save ra, fp",
            "\tsw $fp, 8($sp)\t# save fp",
            "\tsw $ra, 4($sp)\t# save ra",
            "\taddiu $fp, $sp, 8\t# set up new fp",
        ]
        code += function.block.cgen(symbol_table)
        code += [
            "\tmove $sp, $fp\t\t# pop callee frame off stack",
            "\tlw $ra, -4($fp)\t# restore saved ra",
            "\tlw $fp, 0($fp)\t# restore saved fp",
            "\tjr $ra\t\t# return from function",
        ]
        # Reset
        symbol_table.local_offset = 0
        symbol_table.current_scope = curr_scope.parent_scope
        return code

    @staticmethod
    def new_class(symbol_table,class_var): #todo add class model

        #todo where is name of class
        curr_scope = symbol_table.new_scope(name="name")

        code = []
        for var in class_var.vars : #todo add vars class parameter
            curr_scope.add_symbol(symbol_table,class_var)

        for func in class_var.void_funcs : #todo add class parameter
            curr_scope.add_symbol(symbol_table,func)

        for func in class_var.type_funcs : #todo add class parameter
            curr_scope.add_symbol(symbol_table,func)


        # for func in class_var.void_funcs : #todo add  void_funcs class parameter
        #     code +=new_void_function(symbol_table,func)
        #
        # for func in class_var.type_funcs : #todo add type_funcs class parameter
        #     code +=new_function(symbol_table,func)

        symbol_table.current_scope = curr_scope.parent_scope
        pass

    @staticmethod
    def statement_block(symbol_table, block):
        symbol_table.current_scope.block_counter += 1
        new_scope_name = symbol_table.current_scope.name+"_"+"block"+str(symbol_table.current_scope.block_counter)
        curr_scope = symbol_table.new_scope(name=new_scope_name)
        code = []
        print("BLOCK")
        for stm in block.block_statements:
            if type(stm).__name__ == "Variable":
                code += CodeGenerator.new_variable(symbol_table, stm)
            elif type(stm).__name__ == "IfStatement":
                code += CodeGenerator.if_statement(symbol_table, stm)
            elif type(stm).__name__ == "ForStatement":
                code += CodeGenerator.for_statement(symbol_table, stm)
            elif type(stm).__name__ == "PrintNode":
                code += CodeGenerator.print_statement(symbol_table, stm)
            elif type(stm).__name__ == "WhileStatement":
                code += CodeGenerator.while_statement(symbol_table, stm)
            elif type(stm).__name__ == "OptionalExpr":
                code += CodeGenerator.optional_expression_statement(symbol_table, stm)
            elif type(stm).__name__ == "ReturnStatement":
                break
        symbol_table.current_scope = curr_scope.parent_scope
        return code

    @staticmethod
    def optional_expression_statement(symbol_table, op_expr):
        code = []
        if op_expr.expr is not None:
            print(op_expr.expr)
        return code

    @staticmethod
    def if_statement(symbol_table, if_stm):
        symbol_table.current_scope.block_counter += 1
        code = []
        if if_stm.else_block is None:
            code += if_stm.condition.cgen(symbol_table)
            code.append(f"beqz $t1, IF{if_stm.if_id}")
            code += if_stm.block.cgen(symbol_table)
            code.append(f"IF{if_stm.if_id} END:")
        else:
            CodeGenerator.if_statement_with_else(symbol_table, if_stm)
        return code

    @staticmethod
    def if_statement_with_else(symbol_table,if_stm):
        symbol_table.current_scope.block_counter += 1
        code = []
        code += if_stm.condition.cgen(symbol_table)
        code.append(f"beqz $t1, ELSE {if_stm.if_id}")
        code += if_stm.body.cgen(symbol_table)
        code.append(f"j ELSE{if_stm.if_id} END")
        code.append(f"ELSE{if_stm.if_id}:")
        code += if_stm.else_body.cgen(symbol_table)
        code.append(f"ELSE{if_stm.if_id} END:")
        return code

    @staticmethod
    def while_statement(symbol_table, while_stm):
        symbol_table.current_scope.block_counter += 1
        code = [f"LOOP_{while_stm.while_id}:"]
        code += while_stm.condition.cgen(symbol_table)
        code.append(f"\tlw $t1, 4($sp)\t#load expression value from stack to t1")
        code += [
            f"\tlw $t1,4($sp)\t#copy top stack to t1",
            f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
        ]
        code.append(f"\tbeqz $t1,END_LOOP_{while_stm.while_id}")
        code += while_stm.body.cgen(symbol_table)
        code.append(f"END_LOOP_{while_stm.while_id}:")
        return code

    @staticmethod
    def for_statement(symbol_table, for_stm):
        symbol_table.current_scope.block_counter += 1
        code = []
        if for_stm.init is not None:
            code += for_stm.init.cgen(symbol_table)
            code += [
                f"\tlw $t0,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code.append(f"FOR_{for_stm.for_id}:")
        code += for_stm.condition.cgen(symbol_table)
        code += [
            f"\tlw $t1,4($sp)\t#copy top stack to t1",
            f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
        ]
        code.append(f"\tbeqz $t1,END_LOOP_{for_stm.for_id}")
        code += for_stm.block.cgen(symbol_table)
        if for_stm.update is not None:
            code += for_stm.update.cgen(symbol_table)
            code += [
                f"\tlw $t0,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code.append(f"\tj LOOP_{for_stm.for_id}\t# back to start of for")
        code.append(f"END_LOOP_{for_stm.for_id}:")
        return code

    @staticmethod
    def return_statement(symbol_table, return_stm):
        code = []
        if return_stm.statement is not None:
            code += return_stm.expression.cgen(symbol_table)
            if type(return_stm.statement).__name__ == "Const":
                if return_stm.statement.v_type == "double":
                    code += [
                        f"\tl.d $f0,0($sp)# move top stack to f0",
                        f"\taddu $sp,$sp,{double_size}\t# move sp higher cause of pop",
                    ]
                else:
                    code += [
                        f"\tlw $t0,{int_size}($sp)\t#copy top stack to t0",
                        f"\taddu $sp,$sp,{int_size}\t# move sp higher cause of pop",
                    ]
                    code += ["\tmove $v0, $t0\t# Copy return value to $v0"]
        return code

    @staticmethod
    def break_statement(symbol_table, break_stm):
        return [f"j END_LOOP_{break_stm.break_id}"]

    @staticmethod
    def continue_statement(symbol_table):
        pass

    @staticmethod
    def print_statement(symbol_table, print_node):
        code = []
        for expr in print_node.expr:
            print("HERE I AM")
            print(expr)
            code += expr.cgen(symbol_table)
            size = int_size
            if type(expr).__name__ == "Variable" or type(expr).__name__ == "Const":
                if expr.v_type == "int":
                    code.append(f"\tjal _PrintInt")
                elif expr.v_type == "string":
                    code.append(f"\tjal _PrintString")
                elif expr.v_type == "bool":
                    code.append(f"\tjal _PrintBool")
                elif expr.v_type == "double":
                    size = 8
                    code.append(f"\tjal _SimplePrintDouble")

            code.append(f"\taddu $sp,$sp,{size}\t# clean parameters")
        code.append(f"\tjal _PrintNewLine")
        return code

    @staticmethod
    def logical_or(symbol_table, expr):
        code = []
        code += expr.l_operand.cgen(symbol_table)
        code += expr.r_operand.cgen(symbol_table)
        code += [
            f"\tlw $t0,4($sp)\t#copy top stack to t0",
            f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
        ]
        code += [
            f"\tlw $t1,4($sp)\t#copy top stack to t0",
            f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
        ]
        code.append("or $t2,$t1,$t0")
        code += [
            f"\tsubu $sp,$sp,4\t# move sp down cause of push",
            f"\tsw $t2,4($sp)\t#copy t2 to stack",
        ]
        return code

    @staticmethod
    def logical_and(symbol_table, expr):
        code = []
        code += expr.l_operand.cgen(symbol_table)
        code += expr.r_operand.cgen(symbol_table)
        code += [
            f"\tlw $t0,4($sp)\t#copy top stack to t0",
            f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
        ]
        code += [
            f"\tlw $t1,4($sp)\t#copy top stack to t0",
            f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
        ]
        code.append("and $t2,$t1,$t0")
        code += [
            f"\tsubu $sp,$sp,4\t# move sp down cause of push",
            f"\tsw $t2,4($sp)\t#copy t2 to stack",
        ]
        return code

    @staticmethod
    def equals_operation(symbol_table, expr):
        code = []
        code += expr.l_operand.cgen(symbol_table)
        code += expr.r_operand.cgen(symbol_table)
        if expr.l_operand.v_type == "int":
            code += [
                f"\tlw $t0,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code += [
                f"\tlw $t1,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code.append("seq $t2,$t1,$t0")
            code += [
                f"\tsubu $sp,$sp,4\t# move sp down cause of push",
                f"\tsw $t2,4($sp)\t#copy t2 to stack",
            ]
        else:
            counter = symbol_table.get_label()
            code += [
                f"\tl.d $f0,0($sp)# move top stack to f0",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code += [
                f"\tl.d $f2,0($sp)# move top stack to f2",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code.append("c.eq.d $f2,$f0")
            code.append(f"bc1f __double_le__{counter}")
            code.append("li $t0, 1")
            code.append(f"__double_le__{counter}:")
            code += [
                f"\tsubu $sp,$sp,4\t# move sp down cause of push",
                f"\tsw $t0,4($sp)\t#copy t0 to stack",
            ]
        return code

    @staticmethod
    def not_equals_operation(symbol_table, expr):
        code = []
        code += expr.l_operand.cgen(symbol_table)
        code += expr.r_operand.cgen(symbol_table)
        if expr.l_operand.v_type == "int":
            code += [
                f"\tlw $t0,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code += [
                f"\tlw $t1,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code.append("sne $t2,$t1,$t0")
            code += [
                f"\tsubu $sp,$sp,4\t# move sp down cause of push",
                f"\tsw $t2,4($sp)\t#copy t2 to stack",
            ]
        else:
            counter = symbol_table.get_label()
            code += [
                f"\tl.d $f0,0($sp)# move top stack to f0",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code += [
                f"\tl.d $f2,0($sp)# move top stack to f2",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code.append("c.eq.d $f2,$f0")
            code.append(f"bc1t __double_le__{counter}")
            code.append("li $t0, 1")
            code.append(f"__double_le__{counter}:")
            code += [
                f"\tsubu $sp,$sp,4\t# move sp down cause of push",
                f"\tsw $t0,4($sp)\t#copy t0 to stack",
            ]
        return code

    @staticmethod
    def lt_operation(symbol_table, expr):
        code = []
        code += expr.l_operand.cgen(symbol_table)
        code += expr.r_operand.cgen(symbol_table)
        if expr.l_operand.v_type == "int":
            code += [
                f"\tlw $t0,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code += [
                f"\tlw $t1,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code.append("slt $t2,$t1,$t0")
            code += [
                f"\tsubu $sp,$sp,4\t# move sp down cause of push",
                f"\tsw $t2,4($sp)\t#copy t2 to stack",
            ]
        else:
            code += [
                f"\tl.d $f0,0($sp)# move top stack to f0",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code += [
                f"\tl.d $f2,0($sp)# move top stack to f2",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code.append("c.lt.d $f2,$f0")
            code.append(f"bc1f __double_le__")
            #TODO counter
            code.append("li $t0, 1")
            code.append(f"__double_le__:")
            code += [
                f"\tsubu $sp,$sp,4\t# move sp down cause of push",
                f"\tsw $t0,4($sp)\t#copy t0 to stack",
            ]
        return code

    @staticmethod
    def lte_operation(symbol_table, expr):
        code = []
        code += expr.l_operand.cgen(symbol_table)
        code += expr.r_operand.cgen(symbol_table)
        if expr.l_operand.v_type == "int":
            code += [
                f"\tlw $t0,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code += [
                f"\tlw $t1,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code.append("sle $t2,$t1,$t0")
            code += [
                f"\tsubu $sp,$sp,4\t# move sp down cause of push",
                f"\tsw $t2,4($sp)\t#copy t2 to stack",
            ]
        else:
            counter = symbol_table.get_label()
            code += [
                f"\tl.d $f0,0($sp)# move top stack to f0",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code += [
                f"\tl.d $f2,0($sp)# move top stack to f2",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code.append("c.le.d $f2,$f0")
            code.append(f"bc1f __double_le__{counter}")
            code.append("li $t0, 1")
            code.append(f"__double_le__{counter}:")
            code += [
                f"\tsubu $sp,$sp,4\t# move sp down cause of push",
                f"\tsw $t0,4($sp)\t#copy t0 to stack",
            ]
        return code

    @staticmethod
    def gt_operation(symbol_table, expr):
        code = []
        code += expr.l_operand.cgen(symbol_table)
        code += expr.r_operand.cgen(symbol_table)
        if expr.l_operand.v_type == "int":
            code += [
                f"\tlw $t0,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code += [
                f"\tlw $t1,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code.append("sgt $t2,$t1,$t0")
            code += [
                f"\tsubu $sp,$sp,4\t# move sp down cause of push",
                f"\tsw $t2,4($sp)\t#copy t2 to stack",
            ]
        else:
            counter = symbol_table.get_label()
            code += [
                f"\tl.d $f0,0($sp)# move top stack to f0",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code += [
                f"\tl.d $f2,0($sp)# move top stack to f2",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code.append("c.le.d $f2,$f0")
            code.append(f"bc1t __double_le__{counter}")
            code.append("li $t0, 1")
            code.append(f"__double_le__{counter}:")
            code += [
                f"\tsubu $sp,$sp,8",
                f"\ts.d $f0,0($sp)",
            ]
        return code

    @staticmethod
    def gte_operation(symbol_table, expr):
        code = []
        code += expr.l_operand.cgen(symbol_table)
        code += expr.r_operand.cgen(symbol_table)
        if expr.l_operand.v_type == "int":
            code += [
                f"\tlw $t0,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code += [
                f"\tlw $t1,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code.append("sge $t2,$t1,$t0")
            code += [
                f"\tsubu $sp,$sp,4\t# move sp down cause of push",
                f"\tsw $t2,4($sp)\t#copy t2 to stack",
            ]
        else:
            counter = 0
            code += [
                f"\tl.d $f0,0($sp)# move top stack to f0",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code += [
                f"\tl.d $f2,0($sp)# move top stack to f2",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code.append("c.lt.d $f2,$f0")
            code.append(f"bc1t __double_le__{counter}")
            code.append("li $t0, 1")
            code.append(f"__double_le__{counter}:")
        return code

    @staticmethod
    def addition_operation(symbol_table, expr):
        code = []
        code += expr.l_operand.cgen(symbol_table)
        code += expr.r_operand.cgen(symbol_table)
        if expr.l_operand.v_type == "int":
            code += [
                f"\tlw $t0,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code += [
                f"\tlw $t1,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code.append("add $t2,$t1,$t0")
            code += [
                f"\tsubu $sp,$sp,4\t# move sp down cause of push",
                f"\tsw $t2,4($sp)\t#copy t2 to stack",
            ]
        else:
            code += [
                f"\tl.d $f0,0($sp)# move top stack to f0",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code += [
                f"\tl.d $f2,0($sp)# move top stack to f2",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code.append("add.d $f4, $f2, $f0")
            code += [
                f"\tsubu $sp,$sp,8",
                f"\ts.d $f4,0($sp)",
            ]
        return code

    @staticmethod
    def add_plus(symbol_table):
        pass

    @staticmethod
    def subtraction_operation(symbol_table, expr):
        code = []
        code += expr.l_operand.cgen(symbol_table)
        code += expr.r_operand.cgen(symbol_table)
        if expr.l_operand.v_type == "int":
            code += [
                f"\tlw $t0,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code += [
                f"\tlw $t1,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code.append("sub $t2,$t1,$t0")
            code += [
                f"\tsubu $sp,$sp,4\t# move sp down cause of push",
                f"\tsw $t2,4($sp)\t#copy t2 to stack",
            ]
        else:
            code += [
                f"\tl.d $f0,0($sp)# move top stack to f0",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code += [
                f"\tl.d $f2,0($sp)# move top stack to f2",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code.append("sub.d $f4, $f2, $f0")
            code += [
                f"\tsubu $sp,$sp,8",
                f"\ts.d $f4,0($sp)",
            ]
        return code

    @staticmethod
    def minus_plus(symbol_table):
        pass

    @staticmethod
    def multiplication_operation(symbol_table, expr):
        code = []
        code += expr.l_operand.cgen(symbol_table)
        code += expr.r_operand.cgen(symbol_table)
        if expr.l_operand.v_type == "int":
            code += [
                f"\tlw $t0,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code += [
                f"\tlw $t1,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code.append("mul $t2,$t1,$t0")
            code += [
                f"\tsubu $sp,$sp,4\t# move sp down cause of push",
                f"\tsw $t2,4($sp)\t#copy t2 to stack",
            ]
        else:
            code += [
                f"\tl.d $f0,0($sp)# move top stack to f0",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code += [
                f"\tl.d $f2,0($sp)# move top stack to f2",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code.append("mul.d $f4, $f2, $f0")
            code += [
                f"\tsubu $sp,$sp,8",
                f"\ts.d $f4,0($sp)",
            ]
        return code

    @staticmethod
    def mul_plus(symbol_table):
        pass

    @staticmethod
    def division_operation(symbol_table, expr):
        code = []
        code += expr.l_operand.cgen(symbol_table)
        code += expr.r_operand.cgen(symbol_table)
        if expr.l_operand.v_type == "int":
            code += [
                f"\tlw $t0,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code += [
                f"\tlw $t1,4($sp)\t#copy top stack to t0",
                f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
            ]
            code.append("div $t2,$t1,$t0")
            code += [
                f"\tsubu $sp,$sp,4\t# move sp down cause of push",
                f"\tsw $t2,4($sp)\t#copy t2 to stack",
            ]
        else:
            code += [
                f"\tl.d $f0,0($sp)# move top stack to f0",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code += [
                f"\tl.d $f2,0($sp)# move top stack to f2",
                f"\taddu $sp,$sp,8\t# move sp higher cause of pop",
            ]
            code.append("div.d $f4, $f2, $f0")
            code += [
                f"\tsubu $sp,$sp,8",
                f"\ts.d $f4,0($sp)",
            ]
        return code

    @staticmethod
    def divide_plus(symbol_table):
        pass

    @staticmethod
    def modulo_operation(symbol_table, expr):
        code = []
        code += expr.l_operand.cgen(symbol_table)
        code += expr.r_operand.cgen(symbol_table)
        code += [
            f"\tlw $t0,4($sp)\t#copy top stack to t0",
            f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
        ]
        code += [
            f"\tlw $t1,4($sp)\t#copy top stack to t0",
            f"\taddu $sp,$sp,4\t# move sp higher cause of pop",
        ]
        code.append("div $t2,$t1,$t0")
        code.append("mfhi $t2")
        code += [
            f"\tsubu $sp,$sp,4\t# move sp down cause of push",
            f"\tsw $t2,4($sp)\t#copy t2 to stack",
        ]
        return code

    @staticmethod
    def baghi_plus(symbol_table):
        pass

    @staticmethod
    def not_operation(symbol_table):
        pass

    @staticmethod
    def this_expression(symbol_table):
        pass

    @staticmethod
    def read_integer():
        return [
            "jal _ReadInteger",
            "subu $sp,$sp,4 # Make space for Integer.",
            "sw $v0,4($sp)  # Copy Integer to stack.",
        ]

    @staticmethod
    def read_line():
        return [
            "jal _ReadLine",
            "subu $sp,$sp,4 # Make space for Integer.",
            "sw $v0,4($sp)  # Copy Integer to stack.",
        ]

    @staticmethod
    def initiate_class(symbol_table):
        pass

    @staticmethod
    def f(symbol_table):
        pass

    @staticmethod
    def l(self, symbol_table):
        pass

    @staticmethod
    def assignment(symbol_table, variable):
        code = ["assign"]
        print("assign cgen")
        return code

    @staticmethod
    def identifier_l_value(symbol_table):
        pass

    @staticmethod
    def member_access_l_value(symbol_table):
        pass

    @staticmethod
    def array_access_l_value(symbol_table):
        pass

    @staticmethod
    def identifier_l_value(symbol_table):
        pass

    @staticmethod
    def function_call(symbol_table):
        pass

    @staticmethod
    def method_call(symbol_table):
        pass

    @staticmethod
    def identifier(symbol_table):
        pass

    @staticmethod
    def new_identifier(symbol_table):
        pass

    @staticmethod
    def int_const(value):
        print("cgen int const")
        print(value)
        return value

    @staticmethod
    def double_const(value):
        print("cgen bool const")
        print(value)

    @staticmethod
    def bool_const(value):
        code = ["cgen bool const"]
        print("cgen bool const")
        print(value)
        return code

    @staticmethod
    def null_const(symbol_table):
        print("cgen null const")
        print(symbol_table)

    @staticmethod
    def string_const(value):
        print("cgen string const")
        print(value)
        code = ["string const"]
        return code
