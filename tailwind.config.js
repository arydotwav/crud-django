module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html', 
      './templates/**/*.html',
      './static/css/**/*.css',
    
  ],
  theme: {
    extend: {
      screens: {
        'xs': '500px' //media query
      }
    },
  },
  plugins: [],
}