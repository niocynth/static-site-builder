# Static Site Builder

A Python-based static site generator that converts Markdown content and static assets into a complete HTML website. Easily build and deploy your site to GitHub Pages or test locally.

## Features

- Converts Markdown files in the [`content`](content) directory to HTML pages.
- Copies static assets (images, CSS, etc.) from the [`static`](static) directory.
- Outputs the generated site to either the [`public`](public) directory (for local testing) or the [`docs`](docs) directory (for GitHub Pages deployment).
- Supports headings, lists, code blocks, blockquotes, images, links, and inline formatting in Markdown.

## Directory Structure

```
static-site-builder/
├── static/      # Static assets (CSS, images, etc.)
├── content/     # Markdown content files
├── docs/        # Output directory for GitHub Pages
├── public/      # Output directory for local testing
├── src/         # Python source code
├── template.html# HTML template for all pages
├── build.sh     # Build script for GitHub Pages
├── main.sh      # Local test script
├── test.sh      # Run unit tests
└── README.md    # This file
```

## Usage

### Local Testing

To build and serve the site locally:

```sh
./main.sh
```

- This will generate the site in the [`public`](public) directory and start a local server at [http://localhost:8888](http://localhost:8888).

### Deploy to GitHub Pages

To build the site for deployment:

```sh
./build.sh
```

- This will generate the site in the [`docs`](docs) directory, ready to be pushed to GitHub Pages.

## Customization

- Edit [`template.html`](template.html) to change the HTML layout.
- Add Markdown files to [`content`](content) for new pages or blog posts.
- Add images, CSS, or other assets to [`static`](static).

## Testing

Run all unit tests with:

```sh
./test.sh
```

## License

MIT License

---

For more details, see the source code in src/.