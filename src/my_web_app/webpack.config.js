const path = require('path');

module.exports = {
  entry: {
    login: './static/js/login-auth.js',  // Output: login.bundle.js
    firebaseConfig: './static/js/firebase-config.js', //output: firebaseConfig.bundle.js
    stripe: './static/js/stripe.js',
    scripts: './static/js/scripts.js',
    lang: './static/js/lang.js'
  },
  output: {
    filename: '[name].bundle.js', // [name] will be replaced with the entry key
    path: path.resolve(__dirname, 'dist'),
  },
  mode: 'development', // or 'production'
};