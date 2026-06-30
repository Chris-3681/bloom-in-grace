import { useParams } from "react-router-dom";
import Layout from "../components/Layout";
import { products } from "../data/products";
import PayPalButton from "../components/PayPalButton";


function Checkout() {
  console.log(import.meta.env.VITE_PAYPAL_CLIENT_ID);
  const { slug } = useParams();

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

        <div className="mt-10">
          <PayPalButton slug={product.slug} />
        </div>

      </div>
    </Layout>
  );
}

export default Checkout;
