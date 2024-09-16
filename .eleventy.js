const { EleventyRenderPlugin } = require("@11ty/eleventy");
const MarkdownIt = require("markdown-it");


module.exports = function(eleventyConfig) {
  eleventyConfig.addPlugin(EleventyRenderPlugin);
  
  // Markdown options
  const md = new MarkdownIt({
    html: true
  });
  md.use(require("markdown-it-anchor").default);
  md.use(require("markdown-it-table-of-contents"), { includeLevel: [2] });
  eleventyConfig.setLibrary("md", md);

  eleventyConfig.addPassthroughCopy("src/images/");
  // Return your Object options:
  return {
    dir: {
      input: "src",
      output: "_site"
    }
  }
};