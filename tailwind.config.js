module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        sand:  "#FFF2E0",
        lilac: { 200:"#C0C9EE", 300:"#A2AADB", 500:"#898AC4" }
      },
      boxShadow: { soft: "0 2px 10px rgba(0,0,0,0.06)" },
      borderRadius: { xl2: "1rem" }
    },
  },
  plugins: [require("@tailwindcss/forms"), require("@tailwindcss/typography")],
}
