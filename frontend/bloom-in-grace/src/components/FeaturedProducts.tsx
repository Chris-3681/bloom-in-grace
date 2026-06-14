import { products } from "../data/products";
import ProductCard from "./ProductCard";

function FeaturedProducts() {
  return (
    <section className="max-w-7xl mx-auto px-6 py-20">

      <h2 className="text-4xl font-bold text-center text-[#4A3F35]">
        Featured Resources
      </h2>

      <p className="text-center text-[#7B6F63] mt-4">
        Practical tools to help you grow in prayer and Scripture.
      </p>

      <div className="grid md:grid-cols-3 gap-8 mt-12">
        {products.map((product) => (
          <ProductCard
            key={product.id}
            slug={product.slug}
            name={product.name}
            price={product.price}
            description={product.description}
            image={product.image}
          />
        ))}
      </div>

    </section>
  );
}

export default FeaturedProducts;