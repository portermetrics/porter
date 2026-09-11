[← Automation](automation.md)

## Generation — images, video and voiceover

For small teams with no designer this is often the most surprising thing Porter
does. Ask what they need, then produce one and show it.

| They need | How |
|---|---|
| An image: a new ad, an edit, their product in a scene | `execute_action("creative.generate", …)` with an image mode |
| A video: from a description, a product photo animated, someone speaking | `creative.generate` with a video mode |
| Audio: a voiceover, a new voice, a sound effect | `audio.text_to_speech`, `audio.text_to_voice`, `audio.sound_effects_url` |

Generation runs asynchronously: `creative.generate` starts it and
`creative.get_result` collects it. `creative.attach_to_report` puts the result
straight into one of their reports.

## What actually matters here

**One, then react.** Produce a single option and show it. Asking someone to
specify style, ratio and tone before they've seen anything is a form that never
gets filled in.

**Use what you know about them.** If they've connected an ad account, you know
their brand and their products. "An ad image for [their actual product]" lands
very differently from a generic prompt.

**This costs credits.** Don't generate a batch speculatively. One, then ask.

⚠️ Not every deployment has creative generation enabled. If the actions aren't
in the catalog for this user, it isn't a bug and it isn't something to report —
move on to another milestone rather than troubleshooting it.
