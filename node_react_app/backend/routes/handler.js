const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const Schemas = require('../models/Schemas.js');
var fs = require('fs');

// Model
const playerModel = mongoose.model('stats', Schemas);

/* router.get('/get-data', (req, res) => {
    playerModel.find({})
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.log(error);
      })
}); */

router.get('/analysis', (req, res) => {
    playerModel.find({})
      .then((data) => {
        console.log("Data found!");
        res.json(data);
        console.log(data);
      })
      .catch((error) => {
        console.log(error);
      })
});

router.post('/addTweet', (req, res) => {
    res.end('NA');
});

module.exports = router;