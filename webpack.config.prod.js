var path = require('path');
var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

var config = {
    entry: [
      path.resolve(__dirname, './index')
    ],
    module: {
      loaders: [
        {
          test: /js/,
          exclude: /node_modules/,
          loaders: ['babel']
        },
        {
          test: /\.sass$/,
          loader: ExtractTextPlugin.extract('css!sass')
        }
      ]
    },
    output: {
        path: path.resolve(__dirname, 'appengine/static/bundle'),
        publicPath: '/bundle/',
        filename: 'scripts.js',
    },
    plugins: [
      new webpack.DefinePlugin({
        'process.env': {
          'NODE_ENV': 'production'
        }
      }),
      new ExtractTextPlugin('styles.css', {
          allChunks: true
      })
    ]
};
module.exports = config;
