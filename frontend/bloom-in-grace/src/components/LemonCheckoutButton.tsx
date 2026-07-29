import axios from "axios";
import API_URL from "../config/api";

type Props = {
    slug: string;
    email: string;
};

function LemonCheckoutButton({
    slug,
    email,
}: Props) {

    const startCheckout = async () => {

    if (!email.trim()) {
        alert("Please enter your email.");
        return;
    }

    try {

        const response = await axios.post(
        `${API_URL}/create-checkout`,
        {
        slug,
        email
        }
        );

        window.location.href =
        response.data.checkout_url;

    } catch (err) {

    console.error(err);

    alert(
    "Unable to start checkout."
    );

    }

    };

    return (

    <button

        onClick={startCheckout}

        className="w-full rounded-lg bg-[#C9A66B] py-4 text-white text-lg font-semibold hover:opacity-90"

    >

        Buy Now

    </button>

    );

}

export default LemonCheckoutButton;