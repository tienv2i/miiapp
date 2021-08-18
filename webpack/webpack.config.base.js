const path = require('path');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    entry: {
        app: './frontend/app.js',
        home: './frontend/home.js',
    },
    output: {
        path: path.resolve(__dirname, '../frontend/dist'),
        publicPath: '/static/',
        filename: 'js/[name].[hash:8].js'
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
                use: [
                  {
                    loader: 'file-loader',
                    options: {
                        filename: 'images/[name].[hash:8].[ext]'
                    }
                  },
                ],
            },
            {
                test: /\.(woff|ttf|oet)$/i,
                use: [
                  {
                    loader: 'file-loader',
                    options: {
                        filename: 'fonts/[name].[hash:8].[ext]'
                    }
                  },
                ],
            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'css/style.css',
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
          // maxInitialRequests: Infinity,
          // minSize: 0,
          // cacheGroups: {
          //   vendor: {
          //     test: /[\\/]node_modules[\\/]/,
          //     name(module) {
          //       // get the name. E.g. node_modules/packageName/not/this/part.js
          //       // or node_modules/packageName
          //       const packageName = module.context.match(/[\\/]node_modules[\\/](.*?)([\\/]|$)/)[1];
      
          //       // npm package names are URL-safe, but some servers don't like @ symbols
          //       return `npm.${packageName.replace('@', '')}`;
          //     },
          //   },
          // },
        },
    }
}