.globl main
.text
	subu $sp, $sp, 4	# Decrement sp to make space for variable dummyVar.
	subu $sp, $sp, 4	# Decrement sp to make space for variable sum.
add:
	subu $sp, $sp, 8	# decrement sp to make space to save ra, fp
	sw $fp, 8($sp)	# save fp
	sw $ra, 4($sp)	# save ra
	addiu $fp, $sp, 8	# set up new fp
	move $sp, $fp		# pop callee frame off stack
	lw $ra, -4($fp)	# restore saved ra
	lw $fp, 0($fp)	# restore saved fp
	jr $ra		# return from function
