#!/usr/bin/node
const fs = require('fs');
const requests = require('request');
requests(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
