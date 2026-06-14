import Layout from "../components/Layout";
import ProductCard from "../components/ProductCard";
import { products } from "../data/products";

function Shop() {
  return (
    <Layout>
      <section className="max-w-7xl mx-auto px-6 py-20">
        <h1 className="text-5xl font-bold text-[#4A3F35] text-center">
          Shop Resources
        </h1>

        <p className="text-center text-[#7B6F63] mt-4">
          Faith-centered resources designed to strengthen your prayer life,
          Bible study habits, and spiritual growth.
        </p>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mt-12">
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
    </Layout>
  );
}

export default Shop;