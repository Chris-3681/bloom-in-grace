import { Link } from "react-router-dom";

type Product = {
  slug: string;
  name: string;
  price: number;
  description: string;
  image: string;
};

function ProductCard({ slug, name, price, description, image, }: Product) {
  return (
    <div className="bg-white rounded-xl shadow-sm p-6 border border-[#EFE7DE]">

      <img
  src={image}
  alt={name}
  className="w-full h-64 object-cover rounded-lg mb-4"
/>
      <h3 className="text-xl font-semibold text-[#4A3F35]">
        {name}
      </h3>

      <p className="text-[#7B6F63] mt-2">
        {description}
      </p>

      <p className="mt-4 font-bold text-[#C9A66B]">
        ${price}
      </p>

      <Link
  to={`/product/${slug}`}
  className="block mt-4 w-full text-center py-3 bg-[#C9A66B] text-white rounded-lg"
>
  View Product
</Link>

    </div>
  );
}

export default ProductCard;