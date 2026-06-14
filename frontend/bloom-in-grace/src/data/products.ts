import bibleStudyWorkbook from "../assets/products/bible-study-workbook.png";
import gratitudeJournal from "../assets/products/gratitude-journal.png";
import memoryPages from "../assets/products/memory-pages.png";
import prayerTracker from "../assets/products/prayer-tracker.png";

export const products = [
  {
    id: 1,
    slug: "bible-study-workbook",
    name: "30-Day Daily Bible Study Method Pages",
    price: 9.99,
    image: bibleStudyWorkbook,
    pdf: "/products/bible-study-workbook.pdf",
    description:
      "A guided workbook to help women study Scripture consistently and deeply.",
  },

  {
    id: 2,
    slug: "gratitude-journal",
    name: "30-Day Gratitude Journal for Women",
    price: 7.99,
    image: gratitudeJournal,
    pdf: "/products/gratitude-journal.pdf",
    description:
      "Develop a habit of thankfulness through daily guided reflections.",
  },

  {
    id: 3,
    slug: "scripture-memory-pages",
    name: "30-Day Scripture Memory Pages",
    price: 6.99,
    image: memoryPages,
    pdf: "/products/scripture-memory-pages.pdf",
    description:
      "Memorize and meditate on God's Word with structured daily exercises.",
  },

  {
    id: 4,
    slug: "prayer-tracker",
    name: "30-Day Prayer Tracker",
    price: 4.99,
    image: prayerTracker,
    pdf: "/products/prayer-tracker.pdf",
    description:
      "Track prayers, answered prayers, and spiritual growth over 30 days.",
  },
];