import logo from "../assets/logo/bloom-in-grace-logo.png";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-[#FFFDFB] border-b border-[#EFE7DE]">
      <div className="max-w-7xl mx-auto flex items-center justify-between px-6 py-4">
        <Link to="/">
  <img
    src={logo}
    alt="Bloom in Grace"
    className="h-16"
  />
</Link>

        <ul className="flex gap-8 text-[#4A3F35] font-medium">
  <li className="hover:text-[#C9A66B]">
    <Link to="/">Home</Link>
  </li>

  <li className="hover:text-[#C9A66B]">
    <Link to="/shop">Shop</Link>
  </li>

  <li className="hover:text-[#C9A66B]">
    <Link to="/about">About</Link>
  </li>

  <li className="hover:text-[#C9A66B]">
    <Link to="/contact">Contact</Link>
  </li>
</ul>
      </div>
    </nav>
  );
}

export default Navbar;