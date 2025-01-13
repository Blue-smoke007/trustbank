import "./jquery-3.7.1.min.js";

const header = `
<header class="fixed top-0 left-0 z-30 w-full">
  <nav
    class="flex justify-between items-center p-6 bg-[#1F0034] text-white"
  >
    <div class="flex items-center space-x-3">
      <img src="logo.svg" alt="Logo" class="h-8" />
      <span class="text-lg font-semibold tracking-widest">TRUIST</span>
    </div>
    <ul class="flex space-x-6">
      <li><a href="/homepage.html#" class="text-white hover:border-b-2 px-4 py-1">Home</a></li>
      <li>
        <a href="/homepage.html#products" class="text-white hover:border-b-2 px-4 py-1"
          >Products</a
        >
      </li>
      <li>
        <a href="/homepage.html#rewards" class="text-white hover:border-b-2 px-4 py-1"
          >Rewards</a
        >
      </li>
      <li><a href="#" class="text-white hover:border-b-2 px-4 py-1">Contact us</a></li>
      <li><a href="signin.html" class="text-white hover:border-b-2 px-4 py-1">Dashboard</a></li>
    </ul>
  </nav>
</header>
`;

const footer = `
<footer class="bg-[#1F0034] text-white p-6">
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
  <div class="container mx-auto grid grid-cols-1 md:grid-cols-4 gap-8">
      <ul>
        <li>
          <h3 class="text-lg font-bold mb-4">Company</h3>
          <p class="mb-2 hover:underline">About Us</p>
          <p class="mb-2 hover:underline">Leadership</p>
          <p class="mb-2 hover:underline">Careers</p>
          <p class="mb-2 hover:underline">Our Impact</p>
          <p class="mb-2 hover:underline">Contact Us</p>
          <p class="hover:underline">Trust, Safety & Security</p>
        </li>
      </ul>
  
      <ul>
        <li>
          <h3 class="text-lg font-bold mb-4">For Clients</h3>
          <p class="mb-2 hover:underline">How to Hire</p>
          <p class="mb-2 hover:underline">Talent Marketplace</p>
          <p class="mb-2 hover:underline">Project Catalog</p>
          <p class="mb-2 hover:underline">Hire Agency</p>
          <p class="mb-2 hover:underline">Enterprise</p>
          <p class="mb-2 hover:underline">Contract-to-Hire</p>
          <p class="hover:underline">Direct Contracts</p>
        </li>
      </ul>
  
      <ul>
        <li>
          <h3 class="text-lg font-bold mb-4">For Talent</h3>
          <p class="mb-2 hover:underline">How to Find Work</p>
          <p class="mb-2 hover:underline">Direct Contracts</p>
          <p class="hover:underline">Find Freelance Jobs Worldwide</p>
        </li>
      </ul>
  
      <ul>
        <li>
          <h3 class="text-lg font-bold mb-4">For Talent</h3>
          <p class="mb-2 hover:underline">How to Find Work</p>
          <p class="mb-2 hover:underline">Direct Contracts</p>
          <p class="hover:underline">Find Freelance Jobs Worldwide</p>
        </li>
      </ul>
    </div>

  <div class="social-media container mx-auto flex flex-row gap-7 mt-10 items-center justify-center">
        <div class="social-icons">
          <img src="images/Facebook.svg" alt="facebook" />
        </div>
        <div class="social-icons">
          <img src="images/linkedin.svg" alt="" />
        </div>
        <div class="social-icons "><img src="images/twitter.svg" alt="" /></div>
        <div class="social-icons">
          <img src="images/instagram (6).svg" alt="" />
        </div>
      </div>
  <p class="copyright text-center my-4">
    &copy; 2024, Truist. All Rights Reserved.
  </p>
</footer>
`;

const style = $("<link>").attr("href", "./index.css").attr("rel", "stylesheet");
/** Controls **/
$("head").append(style);
$("body").prepend(header);
$("body").append(footer);
