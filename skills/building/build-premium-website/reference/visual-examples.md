# Visual Examples â€” What Each Section Should Look Like

Use this file as a visual sanity check. If the built section doesn't *feel* like one of these mockups, it's wrong.

The **ground-truth reference** is the bundled file `${CLAUDE_SKILL_DIR}/reference/full-reference-app.jsx` plus the matching `full-reference-index.css`, `full-reference-tailwind.config.js`, and `full-reference-index.html`. Open them when you need exact markup. The mockups below are skeletons â€” match the proportions, the spacing, and the visual hierarchy.

---

## Section 1 â€” Navbar

**Desktop (scrolled state):**
```
    â•­â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â•®
    â”‚ â¬¤ BrandName    Home  Services  About  Process  Contact  [CTA â†—]â”‚
    â•°â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â•¯
        â†‘ frosted glass pill, floating 16px from top, centered, max-w-5xl
```

**Desktop (top of page, transparent):**
```
    â¬¤ BrandName    Home  Services  About  Process  Contact  [CTA â†—]
    â†‘ no background, links + brand are WHITE over hero image
```

**Mobile (closed):**
```
    â•­â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â•®
    â”‚ â¬¤ BrandName         [â˜°] â”‚
    â•°â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â•¯
```

**Mobile (open â€” full-screen overlay):**
```
    â•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•—
    â•‘ BrandName                 [âœ•] â•‘
    â•‘                                â•‘
    â•‘  Home          â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€      â•‘
    â•‘  Services      â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€      â•‘
    â•‘  About         â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€      â•‘
    â•‘  Process       â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€      â•‘
    â•‘  Contact       â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€      â•‘
    â•‘                                â•‘
    â•‘  â•­â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â•®   â•‘
    â•‘  â”‚   Get a quote      â†—   â”‚   â•‘
    â•‘  â•°â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â•¯   â•‘
    â•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    â†‘ rounded-b-5xl, slides down from top, deep/90 backdrop
```

---

## Section 2 â€” Hero

```
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚                                                              â”‚
    â”‚   (background photo, darkened 55%, gradient overlay)         â”‚
    â”‚                                                              â”‚
    â”‚                                            Â· Â·               â”‚
    â”‚                                          Â· â¬¤ Â·  â† floating  â”‚
    â”‚                                            Â·                 â”‚
    â”‚                                                              â”‚
    â”‚   EST. 1992 Â· LOCAL                                          â”‚
    â”‚                                                              â”‚
    â”‚   The work you can                                           â”‚
    â”‚   â€•rely on.                          â† serif italic line     â”‚
    â”‚                                                              â”‚
    â”‚   Three decades of craft, every detail measured twice.       â”‚
    â”‚                                                              â”‚
    â”‚   [ Get a quote â†— ]  [ â˜Ž Call +1 555 0123 ]                  â”‚
    â”‚                                                              â”‚
    â”‚                                              â”‚ Scroll        â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    full 100dvh, content bottom-aligned, h1 ~10â€“12rem on desktop
```

---

## Section 3 â€” Features (3 interactive cards)

```
    Heading line â€” serif italic accent
    Subhead paragraph, max-w-2xl

    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚  EYEBROW Â· 01â”‚  â”‚  EYEBROW Â· 02â”‚  â”‚  EYEBROW Â· 03â”‚
    â”‚  Card title  â”‚  â”‚  Card title  â”‚  â”‚  Card title  â”‚
    â”‚              â”‚  â”‚              â”‚  â”‚              â”‚
    â”‚ â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚  â”‚ â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚  â”‚ â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚
    â”‚ â”‚ Stacked  â”‚ â”‚  â”‚ â”‚SIGNATURE â”‚ â”‚  â”‚ â”‚ Cursor + â”‚ â”‚
    â”‚ â”‚ shuffler â”‚ â”‚  â”‚ â”‚ANIMATION â”‚ â”‚  â”‚ â”‚ calendar â”‚ â”‚
    â”‚ â”‚ (3 cards)â”‚ â”‚  â”‚ â”‚(particlesâ”‚ â”‚  â”‚ â”‚ schedulerâ”‚ â”‚
    â”‚ â”‚          â”‚ â”‚  â”‚ â”‚ falling) â”‚ â”‚  â”‚ â”‚          â”‚ â”‚
    â”‚ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚  â”‚ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚  â”‚ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚
    â”‚              â”‚  â”‚              â”‚  â”‚              â”‚
    â”‚ Description  â”‚  â”‚ Description  â”‚  â”‚ Description  â”‚
    â”‚ Â· bullet     â”‚  â”‚ Â· bullet     â”‚  â”‚ Â· bullet     â”‚
    â”‚ Â· bullet     â”‚  â”‚ Â· bullet     â”‚  â”‚ Â· bullet     â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
        â†‘ each card is interactive â€” middle one is the re-skinned signature
```

The middle card (signature animation) example for plumbing:
```
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚ ðŸ’§ ACUTE STANDBY              07 today  â”‚ â† header strip
    â”‚ â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• â”‚ â† pipe with valves
    â”‚   â–¼     â–¼   â–¼      â–¼   â–¼  â–¼       â–¼     â”‚
    â”‚   â–‘     â–‘   â–‘      â–‘   â–‘  â–‘       â–‘     â”‚ â† teardrops falling
    â”‚   â–‘     â–‘   â–‘      â–‘   â–‘  â–‘       â–‘     â”‚
    â”‚  ~~~â—‹~~~~~~~â—‹~~~~~~~â—‹~~~~~~~~~~~~~~~~~  â”‚ â† water surface + ripples
    â”‚ â— Stable Â· monitoring              STABLEâ”‚ â† status strip
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

Same skeleton for **bakery**: oven rack at top, dough drops falling, counter line, "Fresh batch" status. Same skeleton for **electrical**: cable + sparks. Etc.

---

## Section 4 â€” Pillars (animated counters)

```
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚ EYEBROW LABEL  â”‚ EYEBROW LABEL  â”‚ EYEBROW LABEL  â”‚
    â”‚                â”‚                â”‚                â”‚
    â”‚      30+       â”‚     100%       â”‚     24/7       â”‚
    â”‚                â”‚                â”‚                â”‚
    â”‚ years of       â”‚ authorized     â”‚ emergency      â”‚
    â”‚ experience.    â”‚ professionals. â”‚ response.      â”‚
    â”‚ â”€â”€â”€â”€â”€â”€         â”‚ â”€â”€â”€â”€â”€â”€         â”‚ â”€â”€â”€â”€â”€â”€         â”‚ â† sweep line animates
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    numbers count up from 0 when section enters viewport
    soft blurred color blobs in background
```

---

## Section 5 â€” Protocol (sticky stack)

```
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚ EYEBROW Â· 01                          â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚
    â”‚                                       â”‚               â”‚ â”‚
    â”‚ Step title in big                     â”‚  photograph   â”‚ â”‚
    â”‚ display font                          â”‚   of work     â”‚ â”‚
    â”‚                                       â”‚   in context  â”‚ â”‚
    â”‚ Paragraph describing this stage of    â”‚               â”‚ â”‚
    â”‚ the work with specifics.              â”‚               â”‚ â”‚
    â”‚                                       â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚
    â”‚ Â· checkpoint one                                        â”‚
    â”‚ Â· checkpoint two                                        â”‚
    â”‚ Â· checkpoint three                                      â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
       â†‘ as you scroll, this card shrinks, blurs, fades; next card slides over it
       â†‘ sticky-top â€” stays pinned while you scroll past
```

Three of these stack on top of each other as you scroll. Each subsequent card has a different photo and step number.

---

## Section 6 â€” ServicesGrid (dark, 6 tiles)

```
    (full bleed dark background)

         All services â€” your complete partner.

    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚ â–£ Icon      â”‚ â–£ Icon      â”‚ â–£ Icon      â”‚
    â”‚             â”‚             â”‚             â”‚
    â”‚ Service 1   â”‚ Service 2   â”‚ Service 3   â”‚
    â”‚             â”‚             â”‚             â”‚
    â”‚ Short copy  â”‚ Short copy  â”‚ Short copy  â”‚
    â”‚ describing  â”‚ describing  â”‚ describing  â”‚
    â”‚ the work.   â”‚ the work.   â”‚ the work.   â”‚
    â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤  â† 1px white/5 dividers
    â”‚ â–£ Icon      â”‚ â–£ Icon      â”‚ â–£ Icon      â”‚
    â”‚             â”‚             â”‚             â”‚
    â”‚ Service 4   â”‚ Service 5   â”‚ Service 6   â”‚
    â”‚ ...         â”‚ ...         â”‚ ...         â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    on hover: tile bg lifts to white/[0.03], icon scales 1.1
```

---

## Section 7 â€” TrustSignals

```
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚  ðŸ›¡  Badge 1   â”‚  â”‚  ðŸ†  Badge 2   â”‚  â”‚  â±  Badge 3   â”‚
    â”‚  Authorized     â”‚  â”‚  Member of      â”‚  â”‚  30+ years      â”‚
    â”‚  by [body]      â”‚  â”‚  [association]  â”‚  â”‚  in business    â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    white rounded-2xl cards, subtle shadow, hover lift
```

---

## Section 8 â€” ContactForm

```
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚                    â”‚ â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚
    â”‚ Talk to us         â”‚ â”‚ Name              Email        â”‚ â”‚
    â”‚ â”â”â”â”â”â”â”â”â”â”â”        â”‚ â”‚ ___________       ___________  â”‚ â”‚
    â”‚                    â”‚ â”‚                                â”‚ â”‚
    â”‚ â”Œâ”€â”€â”€â” â˜Ž Phone      â”‚ â”‚ Phone             Zip          â”‚ â”‚
    â”‚ â”‚ â˜Ž â”‚ +1 555 0123  â”‚ â”‚ ___________       ___________  â”‚ â”‚
    â”‚ â””â”€â”€â”€â”˜              â”‚ â”‚                                â”‚ â”‚
    â”‚                    â”‚ â”‚ Message                        â”‚ â”‚
    â”‚ â”Œâ”€â”€â”€â” âœ‰ Email      â”‚ â”‚ â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚ â”‚
    â”‚ â”‚ âœ‰ â”‚ hi@co.com   â”‚ â”‚ â”‚                            â”‚ â”‚ â”‚
    â”‚ â””â”€â”€â”€â”˜              â”‚ â”‚ â”‚                            â”‚ â”‚ â”‚
    â”‚                    â”‚ â”‚ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚ â”‚
    â”‚ â”Œâ”€â”€â”€â” ðŸ“ Location  â”‚ â”‚                                â”‚ â”‚
    â”‚ â”‚ ðŸ“â”‚ City, State  â”‚ â”‚ â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚ â”‚
    â”‚ â””â”€â”€â”€â”˜              â”‚ â”‚ â”‚  â¬†  Drop images or browse  â”‚ â”‚ â”‚
    â”‚                    â”‚ â”‚ â”‚     max 5 Â· jpg, png       â”‚ â”‚ â”‚
    â”‚ ðŸ”’ Data is secure  â”‚ â”‚ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚ â”‚
    â”‚    and private.    â”‚ â”‚                                â”‚ â”‚
    â”‚                    â”‚ â”‚ â•­â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â•® â”‚ â”‚
    â”‚                    â”‚ â”‚ â”‚  Send message          â†—   â”‚ â”‚ â”‚
    â”‚                    â”‚ â”‚ â•°â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â•¯ â”‚ â”‚
    â”‚                    â”‚ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    grid lg:grid-cols-12 â€” left col-span-5, right col-span-7
```

**Sent state replaces the form:**
```
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚                                    â”‚
    â”‚              âœ“                     â”‚
    â”‚       Thanks â€” we'll be            â”‚
    â”‚       in touch within              â”‚
    â”‚       one business day.            â”‚
    â”‚                                    â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## Section 9 â€” Footer

```
    (dark bg-deep)
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚                                                               â”‚
    â”‚   Big tagline line in display font, max-w-3xl                 â”‚
    â”‚   â”€ italic serif accent line.                                 â”‚
    â”‚                                                               â”‚
    â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
    â”‚ â¬¤ Brand        Services    Company     Contact                â”‚
    â”‚ â€•italic        Service 1   About       â˜Ž +1 555 0123          â”‚
    â”‚  tagline       Service 2   Process     âœ‰ hi@co.com            â”‚
    â”‚                Service 3   Careers     ðŸ“ City, State         â”‚
    â”‚ â— System       Service 4                                      â”‚
    â”‚   operational  Service 5                                      â”‚
    â”‚   (mono)       Service 6                                      â”‚
    â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
    â”‚ Â© 2026 Brand Â· All rights reserved.    Privacy Â· Terms       â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    5-column grid on desktop, stacks on mobile
    green pulsing dot next to "System operational"
```

---

## Responsive collapse â€” Hero on 375px width

```
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚ â¬¤ BrandName     [â˜°] â”‚
    â”‚                      â”‚
    â”‚ (background photo,   â”‚
    â”‚  full vertical fill) â”‚
    â”‚                      â”‚
    â”‚                      â”‚
    â”‚  EST. 1992 Â· LOCAL   â”‚
    â”‚                      â”‚
    â”‚  The work you        â”‚
    â”‚  can â€•rely on.       â”‚
    â”‚                      â”‚
    â”‚  Three decades of    â”‚
    â”‚  craft, every detail â”‚
    â”‚  measured twice.     â”‚
    â”‚                      â”‚
    â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚
    â”‚  â”‚ Get a quote   â†— â”‚ â”‚
    â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚
    â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚
    â”‚  â”‚ â˜Ž Call          â”‚ â”‚
    â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚
    â”‚                      â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
    h1 drops from 8xl â†’ 5xl
    CTAs stack vertically, full width
```

---

## What "premium" feels like (checklist)

If the site doesn't have **all** of these, it's not done:

- [ ] Generous whitespace â€” `py-32` between sections, `max-w-7xl` container
- [ ] Serif italic accent line on every major heading
- [ ] Mono uppercase tracking-widest eyebrow labels (10px)
- [ ] Floating particles in hero matching the industry theme
- [ ] Smooth GSAP stagger on hero entrance (â‰¥800ms duration)
- [ ] At least one ScrollTrigger-driven reveal that's visible on first scroll
- [ ] Animated counters that tick up on viewport entry
- [ ] Sticky-stack protocol section (the most "premium" feeling element)
- [ ] Signature animation looping in the middle feature card
- [ ] Glass effect on scrolled navbar
- [ ] Magnetic-btn shimmer on every CTA
- [ ] Hover lifts on link rows
- [ ] Live status dot (green pulsing) somewhere in the footer
- [ ] Real photography (Unsplash, not stock-illustration vibes)
- [ ] Noise overlay at 5% mix-blend-mode multiply (subtle texture)
- [ ] Custom thin scrollbar matching brand color

If any of these are missing, the site reads as generic â€” not premium.
