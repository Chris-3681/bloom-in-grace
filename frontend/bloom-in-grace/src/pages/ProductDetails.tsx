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
        <div className="max-w-6xl mx-auto px-6 py-20">
          <h1 className="text-4xl font-bold text-[#4A3F35]">
            Product Not Found
          </h1>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <section className="max-w-7xl mx-auto px-6 py-16">

        <div className="grid lg:grid-cols-2 gap-12 items-start">

          {/* Product Image */}
          <div>
            <img
              src={product.image}
              alt={product.name}
              className="w-full rounded-2xl shadow-lg"
            />
          </div>

          {/* Product Info */}
          <div>

            <h1 className="text-4xl md:text-5xl font-bold text-[#4A3F35]">
              {product.name}
            </h1>

            <div className="flex flex-wrap gap-3 mt-6">
              <span className="bg-[#F8F3EE] px-4 py-2 rounded-full text-sm">
                Instant Download
              </span>

              <span className="bg-[#F8F3EE] px-4 py-2 rounded-full text-sm">
                Printable PDF
              </span>
            </div>

            <p className="mt-6 text-lg text-[#7B6F63] leading-relaxed">
              {product.description}
            </p>

            {product.longDescription && (
              <p className="mt-4 text-[#7B6F63] leading-relaxed">
                {product.longDescription}
              </p>
            )}

            {product.included && (
              <div className="mt-8">
                <h2 className="text-2xl font-semibold text-[#4A3F35] mb-4">
                  What's Included
                </h2>

                <ul className="space-y-3 text-[#7B6F63]">
                  {product.included.map((item, index) => (
                    <li key={index}>
                      ✓ {item}
                    </li>
                  ))}
                </ul>
              </div>
            )}

            <div className="mt-10">
              <p className="text-4xl font-bold text-[#C9A66B]">
                ${product.price}
              </p>

              <button className="mt-6 w-full md:w-auto px-10 py-4 bg-[#C9A66B] text-white rounded-xl font-semibold hover:opacity-90 transition">
                Buy Now
              </button>
            </div>

          </div>
        </div>

        {/* Preview Gallery */}
        {product.previews && (
          <div className="mt-24">

            <h2 className="text-3xl font-bold text-[#4A3F35] text-center mb-10">
              Preview Pages
            </h2>

            <div className="grid md:grid-cols-2 gap-8">
              {product.previews.map((preview, index) => (
                <img
                  key={index}
                  src={preview}
                  alt={`${product.name} Preview ${index + 1}`}
                  className="rounded-2xl shadow-md border"
                />
              ))}
            </div>

          </div>
        )}

      </section>
    </Layout>
  );
}

export default ProductDetails;