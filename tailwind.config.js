/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./home_module/templates/**/*.html",
    "./contact_module/templates/**/*.html",
    "./services_module/templates/**/*.html",
    "./templates/**/*.html",
    "./node_modules/flowbite/**/*.js",
    "./static/css/src/**/*.{html,js,css}",
    "./static/js/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
        'iranyekan': ['Iranyekan', 'sans-serif'],
      },
      colors : {
        'color-footer-1':'FB7F20',
        'color-b':'#E88230',
        'color-bb':'#F5F2F0',
        'color-c':'#005247'
      },
      spacing: {
        '10p':'10%',
      },
    },
  },
  plugins: [require('flowbite/plugin')],
}
