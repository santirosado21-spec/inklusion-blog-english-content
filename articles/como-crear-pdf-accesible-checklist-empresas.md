---
title: "How to Create an Accessible PDF: A Checklist for Organizations"
description: "Checklist for creating and reviewing an accessible PDF: structure, reading order, alternative text, forms, language, and testing before publishing."
datePublished: "2026-08-05"
sourceSlug: "como-crear-pdf-accesible-checklist-empresas"
sourceUrl: "https://inklusion-blog.vercel.app/blog/como-crear-pdf-accesible-checklist-empresas/"
language: "en"
---

# How to Create an Accessible PDF: A Checklist for Organizations

**Direct answer:** to create an accessible PDF, start with a well-structured source document, use real headings and lists, define the language and title, add alternative text, maintain a logical reading order, tag tables and forms, ensure sufficient contrast and clear links, export with tags, and verify the result with automated checking, keyboard navigation, and assistive technology before publishing.

The most costly mistake is treating accessibility as an afterthought, once the PDF already has a hundred pages, complex tables, and a publication date that was "due yesterday." Most of the work must be resolved in Word, InDesign, or another source application; subsequent remediation is reserved for verifying and correcting what the export did not preserve.

## What does it mean for a PDF to be accessible?

An accessible PDF allows its information and functions to be used by people with different needs and navigation methods. This includes people who use screen readers, keyboards, magnification, color adjustments, or voice input, as well as those who need a clear structure to orient themselves.

The technical reference depends on the context and each organization's policy. The [WCAG 2.2 from the World Wide Web Consortium (W3C)](https://www.w3.org/TR/WCAG22/) define accessibility outcomes for web content. The W3C also maintains [specific techniques for PDF documents](https://www.w3.org/WAI/WCAG22/Techniques/#pdf), covering structure, headings, language, alternatives, tables, forms, and links.

This guide is operational in nature—it is not a conformance certification or legal advice. The result must be evaluated according to the content, the audience, the distribution platform, and the applicable requirements.

## Before laying out: decide whether you actually need a PDF

PDF is useful for a fixed, downloadable, signable, or print-ready version. It is not always the best format for a policy that changes every week, an online application, or information that needs to be consulted on a phone.

For public-facing content, HTML generally makes search, adaptation, navigation, and maintenance easier. If you need a PDF, consider also publishing an accessible HTML version and keeping both in sync. Two contradictory versions are not accessibility; they are a new administrative sport.

Ask three questions:

- Does the person need to download, print, or keep a fixed version?
- Could the content be better served as an HTML page or form?
- Is there someone responsible for updating and re-testing the PDF when it changes?

## Create accessibility in the source document

### Use styles, not manual formatting

Mark the title, headings, paragraphs, lists, and quotations with real styles. Text that is large and bold may look like a heading, but a screen reader will not identify it as one if it received only visual formatting. Maintain a logical hierarchy: one H1 for the title, H2 for sections, and H3 for subsections.

### Write links that explain their destination

"See the WCAG 2.2 guide" communicates more than five links labeled "click here." The link text must make sense outside the paragraph. Avoid pasting long URLs as the sole label when a descriptive phrase is sufficient.

### Design for contrast and legibility

Do not use color as the only signal. Ensure sufficient contrast between text and background, a legible size, reasonable spacing, and clear typefaces. Review charts: their data series need labels, patterns, or descriptions—not just red and green.

### Describe images according to their function

A decorative image must be marked as such. An informative image requires an alternative that communicates its purpose, not a mechanical list of objects. For a complex chart, provide a summary and the relevant data in text or an accessible table.

## What the export to PDF must preserve

The W3C documents techniques such as creating tagged documents, providing a title, specifying the language, using headings, marking lists, associating table cells, adding alternatives, and defining form controls. When exporting, confirm at least the following:

- **Tags:** the semantic structure appears as headings, paragraphs, lists, tables, and figures.
- **Reading order:** columns, notes, sidebars, and footers are read in a sequence that preserves meaning.
- **Document title:** the properties contain a useful title and the viewer can display it instead of the file name.
- **Primary language:** it is defined; language changes are identified where the tool allows.
- **Bookmarks:** a long document offers navigation by section.
- **Security:** restrictions do not prevent access via assistive technology.

Open the exported PDF and review its tag tree. The "create tagged PDF" option is a good starting point, not automatic approval.

## How to handle tables and forms

### Tables

Use tables for data, not to arrange visual blocks. Identify row and column headers and verify that the associations remain understandable. If a table requires multiple levels, merged cells, and a separate legend, consider splitting it or presenting a simpler alternative.

### Forms

Every field must have a programmatic label, a logical tab order, instructions, and clear error messages. Controls of the same type need names that distinguish their purpose. The person must be able to complete, review, and submit the form without a mouse.

A scanned printed form with blank lines does not become a digital form simply by being inside a PDF. For frequently used processes, an accessible HTML form generally makes validation, contextual help, and mobile use easier.

## What to do with a scanned PDF

A scan is typically a collection of images. Optical character recognition (OCR) can recover text, but it does not by itself create hierarchy, order, lists, tables, alternatives, or accessible fields.

1. Apply OCR in the correct language.
2. Compare the recognized text with the original, especially figures, names, and symbols.
3. Add tags and define the reading order.
4. Mark decorative images and describe informative ones.
5. Configure the title, language, links, and bookmarks.
6. Test again. OCR without review can misread a date or an amount.

When the source file exists, repairing it and re-exporting is usually more reliable than reconstructing all the semantics on top of a scan.

## Test the PDF in four layers

1. **Automated checking:** identifies missing properties, suspect tags, contrast issues, and other detectable findings. Do not use it as the sole evidence.
2. **Structural inspection:** review tags, headings, lists, tables, figures, and reading order. Verify that the structure corresponds to the visual content.
3. **Mouse-free use:** navigate links and controls using only the keyboard. Confirm that focus is visible and the sequence makes sense.
4. **Assistive technology and visual review:** listen to the document with a screen reader, test search and zoom, and verify that no text is cut off, overlapping, or converted to an image.

Include real tasks: finding a section, interpreting a chart, completing a field, activating a link, and returning to a previous point. The question is not whether the file "passed"; it is whether the person was able to get what they needed.

## Checklist before publishing

- The document has a descriptive title and an understandable file name.
- The primary language is defined.
- The text is selectable and searchable; it is not just an image.
- Headings follow a logical hierarchy.
- Lists, tables, quotations, and paragraphs have correct tags.
- The reading order works on pages with columns or sidebars.
- Informative images have useful alternatives; decorative ones are ignored.
- Links describe their destination.
- Contrast and use of color do not exclude information.
- Tables identify headers and relationships.
- Fields have a label, instructions, error messages, and tab order.
- Long documents include bookmarks.
- Testing was carried out with an automated tool, keyboard, and assistive technology.
- The page where the file is downloaded explains the format, size, and purpose.
- There is someone responsible for correcting and re-publishing.

## A publishing process that avoids rework

Assign responsibilities from the moment of the request. Content delivers structure and alternatives; design ensures legibility; the author uses styles; the person exporting preserves tags; quality assurance runs tests; the site owner replaces previous versions and avoids broken links.

Save an accessible template and a checklist alongside the editorial workflow. Then take a monthly sample of published documents. Measure the percentage approved before publishing, errors by type, correction time, and critical documents still pending. Counting PDFs in a folder does not tell you whether anyone can use them.

To review the full context, integrate this task with a [web accessibility audit](https://inklusion-blog.vercel.app/blog/auditoria-accesibilidad-web-wcag-checklist-mexico/). The best accessible PDF is still hard to find if the download page has an empty link or an inaccessible form.

## Frequently asked questions

### What is an accessible PDF?

It is a document whose structure, content, and controls can be perceived, understood, and operated through different navigation methods, including screen readers and keyboards.

### Is a scanned PDF accessible?

Not on its own. It requires OCR, text correction, structure, reading order, properties, alternatives, and testing.

### Are tags enough?

No. They are essential, but reading order, images, links, forms, contrast, and real navigation must also work correctly.

### How is it tested?

Combine automated checking, structural inspection, keyboard navigation, assistive technology, and visual review with zoom.

### Is it better to publish a PDF or HTML?

HTML is generally more flexible for public-facing and frequently changing information. PDF is useful for fixed or downloadable versions, provided it is accessible and maintained.

## Publishing is the last step, not the first test

An accessible PDF is born in the source, preserves its structure on export, and demonstrates its usefulness through testing. If the team only opens the file and confirms that it "looks fine," they have not yet reviewed it from the perspective of many of the people who will need to use it.

## Are your documents part of an accessible site?

Inklusion evaluates web accessibility and helps identify barriers in pages, content, and digital journeys. A prioritized review makes it possible to fix what is actually preventing people from accessing information or completing a task.

[Learn about Inklusion's web accessibility solutions](https://www.inklusion.com.mx/accesibilidad-web/)
