{
	'targets': [
		{
			'target_name': 'mkfifo',
			'sources': ['src/mkfifo.cpp'],
			'include_dirs': ["<!@(node --no-warnings -p \"require('node-addon-api').include\")"],
			'dependencies': ["<!(node --no-warnings -p \"require('node-addon-api').gyp\")"],
			'conditions': [
				['OS=="mac"', {
					'cflags+': ['-fvisibility=hidden'],
					'xcode_settings': {
					  'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES', # -fvisibility=hidden
					}
				}]
			],
		 	'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
		},
	    {
	      "target_name": "action_after_build",
	      "type": "none",
	      "dependencies": [ "<(module_name)" ],
	      "copies": [
	        {
	          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
	          "destination": "<(module_path)"
	        }
	      ]
	    }
	]
}
