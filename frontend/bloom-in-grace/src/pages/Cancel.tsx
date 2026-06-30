import Layout from "../components/Layout";
import { Link } from "react-router-dom";

function Cancel() {
  return (
    <Layout>
      <div className="max-w-4xl mx-auto py-20 px-6 text-center">
        <h1 className="text-4xl font-bold text-red-600">
          Payment Cancelled
        </h1>

        <p className="mt-4">
          Your order was not completed.
        </p>

        <Link
          to="/shop"
          className="inline-block mt-6 px-6 py-3 bg-amber-700 text-white rounded-lg"
        >
          Return to Shop
        </Link>
      </div>
    </Layout>
  );
}

export default Cancel;