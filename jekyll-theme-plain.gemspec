# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "jekyll-theme-plain"
  spec.version       = "0.1.0"
  spec.authors       = ["yuuki"]
  spec.email         = ["yuuki@yuukikonno.com"]

  spec.summary       = "A plain text-like Jekyll theme for GitHub Pages"
  spec.homepage      = "https://github.com/jekyll-theme-plain/jekyll-theme-plain"
  spec.license       = "CC0"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README)!i) }

  spec.add_runtime_dependency "jekyll", "~> 3.9"

  spec.add_development_dependency "bundler", "~> 1.16"
  spec.add_development_dependency "rake", "~> 12.0"
end
