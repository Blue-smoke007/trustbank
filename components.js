import "./jquery-3.7.1.min.js";

const header = `
<header>
  <nav
    class="flex justify-between items-center p-6 bg-gradient-to-b from-purple-950 to-transparent"
  >
    <div class="flex items-center space-x-3">
      <img src="logo.svg" alt="Logo" class="h-8" />
      <span class="text-lg font-semibold tracking-widest">TRUIST</span>
    </div>
    <ul class="flex space-x-6">
      <li><a href="/homepage.html" class="hover:underline">Home</a></li>
      <li>
        <a href="/homepage.html#products" class="hover:underline"
          >Products</a
        >
      </li>
      <li>
        <a href="#/homepage.html#rewards" class="hover:underline"
          >Rewards</a
        >
      </li>
      <li><a href="#" class="hover:underline">Contact us</a></li>
      <li><a href="signin.html" class="hover:underline">Dashboard</a></li>
    </ul>
  </nav>
</header>
`;

const footer = `
<footer class="bg-[#1F0034] text-white py-6">
  <div
    class="container mx-auto mt-4 md:mt-0 flex justify-center items-center max-md:flex-col gap-12 space-x-4"
  >
    <div class="flex items-center space-x-3">
      <img src="logo.svg" alt="Logo" class="h-8" />
      <span class="text-lg font-semibold tracking-widest">TRUIST</span>
    </div>
    <a href="#" class="text-sm hover:underline">Privacy</a>
    <a href="#" class="text-sm hover:underline">Terms and Conditions</a>
    <a href="#" class="text-sm hover:underline">Fraud & Security</a>
    <a href="#" class="text-sm hover:underline">Disclosures</a>
  </div>
  <hr class="container mx-auto my-8" />

  <div
    class="social-media container mx-auto flex justify-center gap-4 items-center"
  >
    <div class="social-icons">
      <img src="Facebook.svg" alt="facebook" />
    </div>
    <div class="social-icons">
      <img src="linkedin.svg" alt="" />
    </div>
    <div class="social-icons"><img src="twitter.svg" alt="" /></div>
    <div class="social-icons">
      <img src="image/Facebook.svg" alt="" />
    </div>
    <div class="social-icons">
      <img src="instagram (6).svg" alt="" />
    </div>
  </div>
  <p class="copyright text-center my-4">
    &copy; 2024, Truist. All Rights Reserved.
  </p>
</footer>
`;

/** Controls **/
$("body").prepend(header);
$("body").append(footer);
