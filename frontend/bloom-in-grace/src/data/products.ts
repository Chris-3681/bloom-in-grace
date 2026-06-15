import type { Product } from "../types/Product";

import bibleStudyWorkbook from "../assets/products/bible-study-workbook.png";
import gratitudeJournal from "../assets/products/gratitude-journal.png";
import memoryPages from "../assets/products/memory-pages.png";
import prayerTracker from "../assets/products/prayer-tracker.png";

import biblePreview1 from "../assets/previews/bible-study-workbook/preview-1.png";
import biblePreview2 from "../assets/previews/bible-study-workbook/preview-2.png";

import gratitudePreview1 from "../assets/previews/gratitude-journal/preview-1.png";
import gratitudePreview2 from "../assets/previews/gratitude-journal/preview-2.png";

import memoryPreview1 from "../assets/previews/memory-pages/preview-1.png";
import memoryPreview2 from "../assets/previews/memory-pages/preview-2.png";

import prayerPreview1 from "../assets/previews/prayer-tracker/preview-1.png";
import prayerPreview2 from "../assets/previews/prayer-tracker/preview-2.png";

export const products: Product[] = [
  {
    id: 1,
    slug: "bible-study-workbook",
    name: "30-Day Daily Bible Study Method Pages",

    description:
      "Develop a deeper understanding of Scripture through a guided 30-day Bible study journey.",

    longDescription:
      "This workbook helps women study God's Word intentionally through daily guided pages that encourage observation, reflection, application, and prayer.",

    price: 9.99,

    image: bibleStudyWorkbook,

    pdf: "/products/bible-study-workbook.pdf",

    previews: [
      biblePreview1,
      biblePreview2,
    ],

    included: [
      "30 guided Bible study pages",
      "Scripture observation framework",
      "Reflection and application sections",
      "Prayer prompts",
      "Printable PDF format",
      "Instant digital download",
    ],
  },

  {
    id: 2,
    slug: "gratitude-journal",

    name: "30-Day Gratitude Journal for Women",

    description:
      "Cultivate joy and thankfulness through 30 days of intentional gratitude journaling.",

    longDescription:
      "Designed to help women develop a Christ-centered habit of gratitude through guided daily reflections and thoughtful journaling prompts.",

    price: 7.99,

    image: gratitudeJournal,

    pdf: "/products/gratitude-journal.pdf",

    previews: [
      gratitudePreview1,
      gratitudePreview2,
    ],

    included: [
      "30 gratitude journal pages",
      "Daily reflection prompts",
      "Faith-centered encouragement",
      "Space for personal journaling",
      "Printable PDF format",
      "Instant digital download",
    ],
  },

  {
    id: 3,
    slug: "scripture-memory-pages",

    name: "30-Day Scripture Memory Pages",

    description:
      "Build a lasting habit of hiding God's Word in your heart through 30 days of guided Scripture memorization and reflection.",

    longDescription:
      "Designed to help women memorize Scripture effectively through repetition, reflection, and practical application exercises.",

    price: 6.99,

    image: memoryPages,

    pdf: "/products/scripture-memory-pages.pdf",

    previews: [
      memoryPreview1,
      memoryPreview2,
    ],

    included: [
      "30 daily scripture memory pages",
      "Structured memorization exercises",
      "Space for reflection and application",
      "Printable PDF format",
      "Instant digital download",
    ],
  },

  {
    id: 4,
    slug: "prayer-tracker",

    name: "30-Day Prayer Tracker",

    description:
      "Track prayers, answered prayers, and spiritual growth through a structured 30-day prayer journey.",

    longDescription:
      "Stay consistent in prayer while recording prayer requests, breakthroughs, answered prayers, and personal spiritual growth.",

    price: 4.99,

    image: prayerTracker,

    pdf: "/products/prayer-tracker.pdf",

    previews: [
      prayerPreview1,
      prayerPreview2,
    ],

    included: [
      "30 daily prayer tracking pages",
      "Prayer request tracker",
      "Answered prayer section",
      "Reflection pages",
      "Printable PDF format",
      "Instant digital download",
    ],
  },
];