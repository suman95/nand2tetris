# repetetive script generator
gate="Or"
no=16
for k in range(16):
	i = str(k)
	# print(gate+"(a=in["+i+"],b=b["+i+"],out=out["+i+"]);")
	# print(gate+"(in=in["+i+"],out=out["+i+"]);")
	print(gate+"(a=in["+i+"],b=t"+str(k-1)+",out=t"+str(k)+");")