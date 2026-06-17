import { Link } from "react-router-dom";

function Footer() {
  return (
    <footer className="bg-[#4A3F35] text-white mt-20">
      <div className="max-w-7xl mx-auto px-6 py-12">

        <div className="grid md:grid-cols-3 gap-10">

          {/* Brand */}
          <div>
            <h3 className="text-2xl font-bold">
              Bloom in Grace
            </h3>

            <p className="mt-4 text-gray-300">
              Faith-centered resources designed to help women grow through
              prayer, gratitude, Scripture memory, and Bible study.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="font-semibold text-lg mb-4">
              Quick Links
            </h4>

            <ul className="space-y-2">

              <li>
                <Link
                  to="/"
                  className="text-gray-300 hover:text-white"
                >
                  Home
                </Link>
              </li>

              <li>
                <Link
                  to="/shop"
                  className="text-gray-300 hover:text-white"
                >
                  Shop
                </Link>
              </li>

              <li>
                <Link
                  to="/about"
                  className="text-gray-300 hover:text-white"
                >
                  About
                </Link>
              </li>

              <li>
                <Link
                  to="/contact"
                  className="text-gray-300 hover:text-white"
                >
                  Contact
                </Link>
              </li>

            </ul>
          </div>

          {/* Contact */}
          <div>
            <h4 className="font-semibold text-lg mb-4">
              Contact
            </h4>

            <p className="text-gray-300">
              miriamgatei2001@gmail.com
            </p>

            <p className="text-gray-300 mt-2">
              Nairobi, Kenya
            </p>
          </div>

        </div>

        <div className="border-t border-gray-600 mt-10 pt-6 text-center text-gray-400">
          © {new Date().getFullYear()} Bloom in Grace. All rights reserved.
        </div>

      </div>
    </footer>
  );
}

export default Footer;