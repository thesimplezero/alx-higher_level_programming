#!/usr/bin/node

exports.converter = function (base) {
    return (dec) => dec.toString(base);
  };
  