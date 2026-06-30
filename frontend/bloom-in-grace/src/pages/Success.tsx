import { useEffect } from "react";
import { useSearchParams, Link } from "react-router-dom";
import Layout from "../components/Layout";
import API_URL from "../config/api";

function Success() {
  const [searchParams] = useSearchParams();

  const token = searchParams.get("token");

  useEffect(() => {
    if (!token) return;

    window.location.href =
      `${API_URL}/download/${token}`;

  }, [token]);

  const handleDownloadAgain = () => {
    if (!token) return;

    window.location.href =
      `${API_URL}/download/${token}`;
  };

  return (
    <Layout>
      <div className="max-w-4xl mx-auto py-20 px-6 text-center">

        <div className="text-6xl mb-6">
          🎉
        </div>

        <h1 className="text-4xl font-bold text-green-600">
          Thank You For Your Purchase
        </h1>

        <p className="mt-4 text-lg text-[#7B6F63]">
          Your payment was successful and your download should begin automatically.
        </p>

        <p className="mt-2 text-[#7B6F63]">
          If your download does not start within a few seconds,
          use the button below.
        </p>

        {token && (
          <button
            onClick={handleDownloadAgain}
            className="mt-8 px-8 py-3 bg-[#C9A66B] text-white rounded-lg hover:opacity-90"
          >
            Download Again
          </button>
        )}

        <div className="mt-6">
          <Link
            to="/shop"
            className="inline-block px-8 py-3 border border-[#C9A66B] text-[#C9A66B] rounded-lg hover:bg-[#F8F3EE]"
          >
            Continue Shopping
          </Link>
        </div>

        {!token && (
          <p className="mt-8 text-red-600">
            Download token missing. Please contact support if payment was completed.
          </p>
        )}

      </div>
    </Layout>
  );
}

export default Success;