import axios from "axios";
import { useNavigate } from "react-router-dom";
import { PayPalButtons } from "@paypal/react-paypal-js";

import API_URL from "../config/api";

type PayPalButtonProps = {
  slug: string;
  email: string;
};

function PayPalButton({
  slug,
  email,
}: PayPalButtonProps) {

  const navigate = useNavigate();

  return (
    <PayPalButtons
      disabled={!email}

      style={{
        layout: "vertical",
        color: "gold",
        shape: "rect",
        label: "paypal",
      }}

      createOrder={async () => {

        const response = await axios.post(
          `${API_URL}/create-paypal-order`,
          {
            slug,
            email,
          }
        );

        return response.data.id;
      }}

      onApprove={async (data) => {

        const response = await axios.post(
          `${API_URL}/capture-paypal-order`,
          {
            orderID: data.orderID,
            slug,
            email,
          }
        );

        navigate("/success");

      }}

      onCancel={() => {

        navigate("/cancel");

      }}

      onError={(err) => {

        console.error("PayPal Error:", err);

      }}

    />
  );
}

export default PayPalButton;