"use strict";

var fs = require('fs');
var _ = require('lodash');
var Moniker = require('moniker');

var outfile = "machines.csv";

var maxArrayLength = 8;

var createHeaderLine = function(arrayLength){
    var headerRow = ["name", "value"];
    for(var i = 0; i < arrayLength; i++){
        headerRow.push("charge[]");
    }
    for(var i = 0; i < arrayLength; i++) {
        headerRow.push("overcharge[]");
    }

    return headerRow.join();
};

var headerLine = createHeaderLine(maxArrayLength);

var options = [
    "option1",
    "option2",
    "option3",
    "option4",
    "option5",
    "option6"
];

var names = Moniker.generator([Moniker.adjective, Moniker.noun]);

var buildChargeArray = function(chargeFrequencyArray, index, options){
    var charges = [];
    chargeFrequencyArray.forEach(function(offset){
        var offsetIndex = (offset + index) % options.length;
        charges.push(options[offsetIndex]);
    });
    return charges;
};

var createCards = function(pointValue, chargeFrequencyArray, overchargeFrequencyArray, options){
    var cards = [];
    for(var index = 0; index < options.length; index++){
        var name = names.choose();
        var charge = buildChargeArray(chargeFrequencyArray, index, options);
        var overcharge = buildChargeArray(overchargeFrequencyArray, index, options);
        cards.push({
            name: name,
            value: pointValue,
            charge: charge,
            overcharge: overcharge
        });
    }
    return cards;
};

var convertArrayToCsv = function(jsonArray, arrayLength) {
    var padLength = arrayLength - jsonArray.length;
    for(var i = 0; i < padLength; i++) {
        jsonArray.push("");
    }
    return jsonArray.join();
};

var convertCardToCsvLine = function(card, arrayLength) {
    return [
        JSON.stringify(card.name),
        JSON.stringify(card.value),
        convertArrayToCsv(card.charge, arrayLength),
        convertArrayToCsv(card.overcharge, arrayLength)
    ].join();
};



var cards  = [].concat(
    createCards(3, [0, 0, 1, 2], [0, 3], options),
    createCards(4, [0, 0, 1, 3, 5], [0, 4], options),
    createCards(5, [0, 0, 0, 2, 2, 2], [5, 5], options),
    createCards(5, [0, 1, 2, 3, 4, 5], [1, 2], options),
    createCards(1, [0, 0], [1, 2, 3, 4, 5], options),
    createCards(2, [0, 1, 2], [3, 3], options),
    createCards(6, [0, 0, 1, 2, 3, 3, 4], [0, 4, 5], options),
    createCards(6, [0, 1, 1, 1, 5, 5, 5], [0, 2, 3, 4], options),
    createCards(8, [0, 1, 1, 1, 2, 3, 4, 5], [0], options),
    createCards(5, [0, 0, 0, 0], [1, 4, 5], options)
);

var wstream = fs.createWriteStream('containers.csv');
wstream.write(headerLine);
wstream.write("\n");

cards.forEach(function(card){
    wstream.write(convertCardToCsvLine(card, maxArrayLength));
    wstream.write("\n");
});

wstream.end();
