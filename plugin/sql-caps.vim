let g:sql_caps_script_path = expand('<sfile>:p:h') . '/sql_caps.py'
if !has('python') && !has('python3')
	echo "Error: SqlCaps requires vim compiled with +python or +python3"
	finish
endif

function! SqlCaps()
	execute (has('python3') ? 'py3file' : 'pyfile') g:sql_caps_script_path
endfunction
