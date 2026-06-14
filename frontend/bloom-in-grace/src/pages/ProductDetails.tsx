import { useParams } from "react-router-dom";
import Layout from "../components/Layout";
import { products } from "../data/products";

function ProductDetails() {
  const { slug } = useParams();

  const product = products.find(
    (item) => item.slug === slug
  );

  if (!product) {
    return (
      <Layout>
        <h1>Product not found</h1>
      </Layout>
    );
  }

  return (
    <Layout>
      <section className="max-w-6xl mx-auto px-6 py-20">

        <div className="grid md:grid-cols-2 gap-12">

          <img
            src={product.image}
            alt={product.name}
            className="w-full rounded-xl"
          />

          <div>

            <h1 className="text-4xl font-bold text-[#4A3F35]">
              {product.name}
            </h1>

            <p className="mt-6 text-[#7B6F63]">
              {product.description}
            </p>

            <p className="mt-6 text-3xl font-bold text-[#C9A66B]">
              ${product.price}
            </p>

            <button className="mt-8 px-8 py-4 bg-[#C9A66B] text-white rounded-lg">
              Buy Now
            </button>

          </div>

        </div>

      </section>
    </Layout>
  );
}

export default ProductDetails;