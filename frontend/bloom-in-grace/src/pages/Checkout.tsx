import { useParams } from "react-router-dom";
import { useState } from "react";
import Layout from "../components/Layout";
import { products } from "../data/products";
import PayPalButton from "../components/PayPalButton";

function Checkout() {
  const { slug } = useParams();

  const [email, setEmail] = useState("");

  const product = products.find(
    (item) => item.slug === slug
  );

  if (!product) {
    return (
      <Layout>
        <div className="max-w-4xl mx-auto py-20 px-6">
          <h1 className="text-4xl font-bold">
            Product Not Found
          </h1>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="max-w-4xl mx-auto py-20 px-6">

        <h1 className="text-4xl font-bold text-[#4A3F35]">
          Checkout
        </h1>

        <div className="mt-10 bg-white border border-[#EFE7DE] rounded-2xl p-6">

          <div className="flex gap-6 items-start">

            <img
              src={product.image}
              alt={product.name}
              className="w-32 rounded-lg"
            />

            <div>

              <h2 className="text-2xl font-semibold text-[#4A3F35]">
                {product.name}
              </h2>

              <p className="mt-2 text-[#7B6F63]">
                {product.description}
              </p>

              <p className="mt-4 text-3xl font-bold text-[#C9A66B]">
                ${product.price}
              </p>

            </div>

          </div>

        </div>

        <div className="mt-8">

          <label className="block text-sm font-medium text-[#4A3F35] mb-2">
            Email Address
          </label>

          <input
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full rounded-lg border border-[#D8CFC4] px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#C9A66B]"
          />

          <p className="text-sm text-gray-500 mt-2">
            Your purchase receipt and future downloads will be linked to this email.
          </p>

        </div>

        <div className="mt-10">

          <PayPalButton
            slug={product.slug}
            email={email}
          />

        </div>

      </div>
    </Layout>
  );
}

export default Checkout;