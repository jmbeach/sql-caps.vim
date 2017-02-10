if !has('python')
	echo "Error: SqlCaps requires vim compiled with +python"
	finish
endif

function! SqlCaps()

python << EOF
import vim, string, re
sqlWords = [
	"create",
	"alter",
	"update",
	"delete",
	"view",
	"select",
	"left", 
	"on", 
	"as", 
	"join",
	"group by",
	"insert",
	"table",
	"column",
	"into",
	"where",
	"if",
	"begin",
	"end",
	"from",
	"go",
	"or",
	"null",
	"is"
]
for i in range(0, len(vim.current.buffer)):
	line = vim.current.buffer[i]
	for sqlWord in sqlWords:
		line = re.sub(r"\b"+sqlWord+r"\b", sqlWord.upper(), line)
	vim.current.buffer[i] = line
EOF
endfunction
