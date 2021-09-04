const path = require('path');
const { merge } = require('webpack-merge');
module.exports = merge(require('./webpack.config.base'), {
    devServer: {
        contentBase: path.join(__dirname, '../frontend/dist'),
        compress: true,
        port: 9000,
        writeToDisk: true,
        watchContentBase: true,
    }
});
