const Path			= require('path')
const Binary		= require('@mapbox/node-pre-gyp')
console.log(Path.resolve(Path.join(__dirname,'./package.json')))
const binding_path	= Binary.find(Path.resolve(Path.join(__dirname,'./package.json')))

module.exports = require(binding_path)