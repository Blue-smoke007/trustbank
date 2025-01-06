/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./pages/**/*.{html,js}", "index.html"],
  theme: {
    extend: {
      colors: {
        primary: "hsl(var(--primary))",
      },
    },
  },
  plugins: [],
};
