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

/** Controls **/
$("body").prepend(header);
