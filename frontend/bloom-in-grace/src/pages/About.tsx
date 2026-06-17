import Layout from "../components/Layout";
import miriamPhoto from "../assets/miriam/miriam-wambui.jpg";

function About() {
  return (
    <Layout>
      <section className="bg-[#FFFDFB]">

        {/* Hero Section */}
        <div className="max-w-6xl mx-auto px-6 py-20 text-center">

          <h1 className="text-5xl md:text-6xl font-bold text-[#4A3F35]">
            Meet the Heart Behind Bloom in Grace
          </h1>

          <p className="mt-8 text-xl text-[#7B6F63] max-w-3xl mx-auto leading-relaxed">
            Bloom in Grace was born from a simple but life-changing realization:
            growth is a journey, and no one should have to walk it alone.
          </p>

        </div>

        {/* About Miriam */}
        <div className="max-w-6xl mx-auto px-6 py-16">

          <div className="grid lg:grid-cols-2 gap-12 items-center">

            <div>
                <img
                src={miriamPhoto}
                alt="Miriam Wambui"
                className="w-full rounded-3xl shadow-lg object-cover max-h-[600px]"
                />
                <div className="mt-4 bg-[#F8F3EE] p-6 rounded-2xl">
  <h3 className="font-semibold text-xl text-[#4A3F35]">
    Miriam Wambui
  </h3>

  <p className="mt-2 text-[#7B6F63]">
    Founder, Bloom in Grace
  </p>
</div>
            </div>
            

            {/* Story */}
            <div>

              <h2 className="text-4xl font-bold text-[#4A3F35]">
                Hi, I'm Miriam
              </h2>

              <p className="mt-6 text-[#7B6F63] leading-relaxed">
                Like many women, I've experienced seasons of waiting,
                uncertainty, stretching, and growth. There were times when
                I needed guidance, encouragement, and practical tools to help
                me stay rooted in my faith while becoming the person God was
                shaping me to be.
              </p>

              <p className="mt-4 text-[#7B6F63] leading-relaxed">
                Through those seasons, I learned something powerful:
                grace isn't about having everything figured out.
                It's about trusting God while you're growing.
              </p>

              <p className="mt-4 text-[#7B6F63] leading-relaxed">
                Bloom in Grace was created from that belief.
              </p>

            </div>

          </div>

        </div>

        {/* Mission */}
        <div className="bg-[#F8F3EE] py-20">

          <div className="max-w-5xl mx-auto px-6 text-center">

            <h2 className="text-4xl font-bold text-[#4A3F35]">
              Our Mission
            </h2>

            <p className="mt-6 text-xl text-[#7B6F63] leading-relaxed">
              To inspire, equip, and encourage women to grow spiritually,
              personally, and purposefully through practical,
              faith-centered resources.
            </p>

          </div>

        </div>

        {/* Core Beliefs */}
        <div className="max-w-6xl mx-auto px-6 py-20">

          <h2 className="text-4xl font-bold text-center text-[#4A3F35]">
            What We Believe
          </h2>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mt-12">

            <div className="bg-white border rounded-2xl p-6 shadow-sm">
              <h3 className="font-semibold text-xl text-[#4A3F35]">
                Your Faith Matters
              </h3>
            </div>

            <div className="bg-white border rounded-2xl p-6 shadow-sm">
              <h3 className="font-semibold text-xl text-[#4A3F35]">
                Your Growth Matters
              </h3>
            </div>

            <div className="bg-white border rounded-2xl p-6 shadow-sm">
              <h3 className="font-semibold text-xl text-[#4A3F35]">
                Your Healing Matters
              </h3>
            </div>

            <div className="bg-white border rounded-2xl p-6 shadow-sm">
              <h3 className="font-semibold text-xl text-[#4A3F35]">
                Your Purpose Matters
              </h3>
            </div>

          </div>

        </div>

        {/* Why Bloom in Grace */}
        <div className="bg-[#F8F3EE] py-20">

          <div className="max-w-5xl mx-auto px-6">

            <h2 className="text-4xl font-bold text-center text-[#4A3F35]">
              Why Bloom in Grace?
            </h2>

            <p className="mt-8 text-[#7B6F63] leading-relaxed text-lg text-center">
              Growth rarely happens overnight. It happens through small,
              faithful steps taken consistently over time.
            </p>

            <div className="grid md:grid-cols-2 gap-6 mt-12">

              <div className="bg-white rounded-2xl p-6">
                ✓ Build meaningful spiritual habits
              </div>

              <div className="bg-white rounded-2xl p-6">
                ✓ Deepen your understanding of Scripture
              </div>

              <div className="bg-white rounded-2xl p-6">
                ✓ Stay consistent in prayer
              </div>

              <div className="bg-white rounded-2xl p-6">
                ✓ Live with greater purpose and intention
              </div>

            </div>

          </div>

        </div>

        {/* Prayer Section */}
        <div className="max-w-5xl mx-auto px-6 py-20 text-center">

          <h2 className="text-4xl font-bold text-[#4A3F35]">
            My Prayer For You
          </h2>

          <p className="mt-8 text-lg text-[#7B6F63] leading-relaxed">
            I pray that when you encounter Bloom in Grace, you find more
            than beautiful resources. I pray you find hope, encouragement,
            and practical tools that help you grow into the person God
            created you to be.
          </p>

          <p className="mt-6 text-lg text-[#7B6F63] leading-relaxed">
            Because blooming isn't about perfection.
            It's about trusting God through every season and believing that
            even the hardest chapters can produce something beautiful.
          </p>

        </div>

        {/* CTA */}
        <div className="bg-[#4A3F35] text-white py-20 text-center">

          <div className="max-w-4xl mx-auto px-6">

            <h2 className="text-4xl font-bold">
              Your Season To Bloom Starts Here
            </h2>

            <p className="mt-6 text-lg text-gray-300">
              Explore faith-centered resources designed to help you grow in
              prayer, gratitude, Scripture memory, and intentional Bible study.
            </p>

            <a
              href="/shop"
              className="inline-block mt-8 bg-[#C9A66B] px-8 py-4 rounded-xl font-semibold"
            >
              Explore Resources
            </a>

          </div>

        </div>

      </section>
    </Layout>
  );
}

export default About;