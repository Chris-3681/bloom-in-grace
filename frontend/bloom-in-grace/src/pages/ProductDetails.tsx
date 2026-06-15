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
        <div className="max-w-4xl mx-auto px-6 py-20">
          <h1 className="text-4xl font-bold">
            Product Not Found
          </h1>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <section className="max-w-6xl mx-auto px-6 py-20">
        <div className="grid md:grid-cols-2 gap-12">

          {/* Product Image */}
          <div>
            <img
              src={product.image}
              alt={product.name}
              className="w-full rounded-xl shadow-md"
            />
          </div>

          {/* Product Information */}
          <div>

            <h1 className="text-4xl font-bold text-[#4A3F35]">
              {product.name}
            </h1>

            <p className="mt-6 text-[#7B6F63] leading-relaxed">
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

                <ul className="space-y-2 text-[#7B6F63]">
                  {product.included.map((item, index) => (
                    <li key={index}>
                      ✓ {item}
                    </li>
                  ))}
                </ul>
              </div>
            )}

            <div className="mt-8 flex gap-4 text-sm">
              <span className="px-3 py-1 bg-[#F8F3EE] rounded-full">
                Instant Download
              </span>

              <span className="px-3 py-1 bg-[#F8F3EE] rounded-full">
                Printable PDF
              </span>
            </div>

            <p className="mt-8 text-4xl font-bold text-[#C9A66B]">
              ${product.price}
            </p>

            <button className="mt-8 px-8 py-4 bg-[#C9A66B] text-white rounded-lg hover:opacity-90 transition">
              Buy Now
            </button>

          </div>
        </div>

        {/* Preview Pages */}
        {product.previews && (
          <div className="mt-20">

            <h2 className="text-3xl font-bold text-[#4A3F35] mb-8 text-center">
              Preview Pages
            </h2>

            <div className="grid md:grid-cols-2 gap-8">
              {product.previews.map((preview, index) => (
                <img
                  key={index}
                  src={preview}
                  alt={`Preview ${index + 1}`}
                  className="rounded-xl border shadow-sm"
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