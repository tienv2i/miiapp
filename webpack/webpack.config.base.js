const path = require('path');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    entry: {
        app: './frontend/src/app.js',
        home: './frontend/src/home.js',
    },
    output: {
        path: path.resolve(__dirname, '../frontend/dist'),
        publicPath: '/static/',
        filename: 'js/[name].[fullhash:8].js',
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                loader: 'babel-loader'
            },
            {
                test: /\.(sa|sc|c)ss$/,
                use: [
                  MiniCssExtractPlugin.loader,
                  "css-loader",
                  "postcss-loader",
                  "sass-loader",
                ],
            },
            {
                test: /\.(png|jpe?g|gif|svg)$/i,
                type: 'asset/resource',
		generator: {
			filename: 'img/[filename][fullhash:8].[ext]'
		}
            },
            {
                test: /\.(woff|ttf|oet)$/i,
                type: 'asset/resource',
		generator: {
			filename: 'fonts/[filename][fullhash:8].[ext]'
		}

            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
		filename: 'css/style.[fullhash:8].css',
        }),
        new CleanWebpackPlugin(),
        new BundleTracker({
            filename: './frontend/webpack-stats.json'
        })
    ],
    optimization: {
        runtimeChunk: 'single',
        splitChunks: {
          chunks: 'all',
        },
    },
}
