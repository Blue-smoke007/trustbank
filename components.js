import "./jquery-3.7.1.min.js";
import "https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js";

const header = `
<header class="fixed top-0 left-0 z-30 w-full">
  <nav
    class="flex justify-between items-center p-6 bg-[#1F0034] text-white"
  >
    <div class="flex items-center space-x-3">
      <img src="images/logo.jpg" alt="Logo" class="h-8" />
      <!-- <span class="text-lg font-semibold tracking-widest">TRUIST</span> -->
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
<div class="mb-24"></div>
`;

const footer = `
<footer class="bg-[#1F0034] text-white p-6 mt-6">
  <div class="container mx-auto mt-4 md:mt-0 flex justify-center items-center max-md:flex-col gap-12 space-x-4">
    <div class="flex items-center space-x-3">
      <img src="images/logo.jpg" alt="Logo" class="h-8" />
      <!-- <span class="text-lg font-semibold tracking-widest">TRUIST</span> -->
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
    &copy; 2024, Unity. All Rights Reserved.
  </p>
</footer>
`;

const sidebarLinks = [
  {
    name: "Dashboard",
    href: "account.html",
  },
  {
    name: "Transactions",
    href: "transaction.html",
  },
  {
    name: "Manage cards",
    href: "card.html",
  },
  {
    name: "Notifications",
    href: "#",
  },
  {
    name: "Help center",
    href: "#",
  },
  {
    name: "Settings",
    href: "#",
  },
];
const sidebar = `
<aside class="w-1/4 bg-white rounded-lg shadow-xl p-6 space-y-4 ">
  <div class="text-center font-[Montserrat] text-lg w-full">
    <img src="images/logo.jpg" className="rounded-lg overflow-hidden"/>
    <hr />
    <nav class="space-y-16 h-full">
      <ul class="flex flex-col justify-between h-full py-2 gap-2">
      ${sidebarLinks
        .map(
          (link) => `
          <li>
            <a href="${
              link.href
            }" class="block p-2 hover:text-purple-600 border rounded-lg hover:border-current ${
            window.location.pathname.slice(1) === link.href
              ? "text-purple-600 border-current"
              : "border-transparent"
          }">${link.name}</a>
          </li>
        `
        )
        .join("")}
        <hr />
        <li>
            <button class="logout block w-full p-2 hover:text-purple-600 border rounded-lg hover:border-current border-transparent"
              >Sign out</a>
          </li>
      </ul>
    </nav>
  </div>
</aside>
`;

const modal = `
<div
  class="modal hidden fixed inset-0 bg-black/90 justify-center items-center"
></div>`;

const loadingModal = (text = "Loading...") => `
  <div class="login-modal-content w-96 h-60 bg-white rounded-md flex gap-2 justify-center items-center text-4xl">
    ${text}
    <svg class="animate-spin size-8 " xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
  </div>`;

const successModal = (text = "Success") => `
  <div class="login-modal-content w-96 h-60 bg-white rounded-md flex justify-center items-center text-4xl text-green-500">
    ${text}
  </div>`;
const errorModal = (text = "Error. Please try again") => `
  <div class="login-modal-content w-96 h-60 bg-white rounded-md flex justify-center items-center text-4xl text-red-500">
    ${text}
  </div>`;

const modalMapping = {
  error: errorModal,
  success: successModal,
  loading: loadingModal,
};

function toggleModal(show = true, modal = "loading", elementText) {
  document.body.style.overflow = show ? "hidden" : "auto";
  const modalElement = document.querySelector(".modal");

  if (show) {
    modalElement.classList.add("flex");
    modalElement.classList.remove("hidden");
    modalElement.innerHTML = modalMapping[modal](elementText);
  } else {
    modalElement.classList.add("hidden");
    modalElement.classList.remove("flex");
  }
}

const style = $("<link>").attr("href", "./index.css").attr("rel", "stylesheet");

const api = axios.create({
  baseURL: "https://nexusbank-backend.onrender.com",
});

async function login(formData) {
  toggleModal(true, "loading", "Logging in");

  try {
    const response = await api.post("/login/", formData);
    setAuth(response.data);
    toggleModal(true, "success");
    setTimeout(() => {
      toggleModal(false);
      window.location.href = isAdmin() ? "admin.html" : "account.html";
    }, 3000);
  } catch (error) {
    console.log(error);
    toggleModal(true, "error");
    setTimeout(() => toggleModal(false), 3000);
  }
}

function logout() {
  setAuth(null);
  window.location.href = "homepage.html";
}

function getAuth() {
  try {
    return JSON.parse(localStorage.getItem("_auth"));
  } catch (err) {
    return false;
  }
}

function setAuth(auth) {
  try {
    localStorage.setItem("_auth", JSON.stringify(auth));
    return true;
  } catch (err) {
    return false;
  }
}

function isAdmin() {
  const admins = [
    "neroblue007@gmail.com",
    "shedrackifeanyi2040@gmail.com",
    "cadomint@gmail.com",
  ];
  const auth = getAuth();
  return admins.includes(auth?.user?.email);
}

/** Controls **/
document.addEventListener("DOMContentLoaded", () => {
  $("head").append(style);
  $("body").prepend(header);
  $("body").append(footer);
  $("body").append(modal);
  $(".sidebar").replaceWith($(sidebar));
  $(".logout").on("click", logout);

  window.onComponentLoaded?.({
    getAuth,
    setAuth,
    toggleModal,
    login,
    api,
  });
});
