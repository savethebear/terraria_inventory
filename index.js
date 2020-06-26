const express = require('express');
const path = require('path');

const index_router = require('./routes/index');

const app = express();

app.use(express.static(path.join(__dirname, 'public')));

app.use('/', index_router);

module.exports = app;