
    const navLinks = document.querySelectorAll("nav a");
    const sections = document.querySelectorAll("section");

    navLinks.forEach(link => {
      link.addEventListener("click", () => {
        // remove active classes
        navLinks.forEach(nav => nav.classList.remove("active"));
        sections.forEach(sec => sec.classList.remove("active"));

        // add active to clicked nav and target section
        link.classList.add("active");
        const target = document.getElementById(link.dataset.target);
        target.classList.add("active");
      });
    });

// student-dashboard

 function showSection(id) {
      document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
      document.getElementById(id).classList.add('active');
 }

    // Chart.js 
  const subjects = ["COS 201", "SEN 201", "ENT 211", "IFT 211", "IFT 203", "IFT 205", "NAUB IFT-211"];
  const scores = [75, 37, 80, 74, 82, 70, 70];
  const creditUnits = [3, 2, 2, 2, 2, 2, 3];

  const grades = [];
  const weightedPoints = [];
  let totalPoints = 0, totalUnits = 0;

  // Grade calculator
  function getGrade(score) {
    if (score >= 70) return { grade: "A", point: 5, remark: "Excellent 🎉" };
    if (score >= 60) return { grade: "B", point: 4, remark: "Very Good 👍" };
    if (score >= 50) return { grade: "C", point: 3, remark: "Good 👌" };
    if (score >= 45) return { grade: "D", point: 2, remark: "Fair 😐" };
    if (score >= 40) return { grade: "E", point: 1, remark: "Pass ⚠️" };
    return { grade: "F", point: 0, remark: "Fail ❌" };
  }

  // Build table dynamically
  const tableBody = document.getElementById("resultsTableBody");
  scores.forEach((score, i) => {
    const { grade, point } = getGrade(score);
    grades.push(grade);
    let wPoint = point * creditUnits[i];
    weightedPoints.push(wPoint);

    totalPoints += wPoint;
    totalUnits += creditUnits[i];

    // Add row to table
    let row = `
      <tr data-index="${i}">
        <td>${subjects[i]}</td>
        <td>${score}</td>
        <td>${grade}</td>
        <td>${creditUnits[i]}</td>
        <td>${wPoint}</td>
      </tr>`;
    tableBody.innerHTML += row;
  });

  // GPA Calculation
  let gpa = (totalPoints / totalUnits).toFixed(2);
  document.getElementById("gpaResult").innerText = `GPA: ${gpa} (on a 5.0 scale)`;


    // Main Chart
  const ctx = document.getElementById("resultsChart").getContext("2d");
  new Chart(ctx, {
    type: "line",
    data: {
      labels: subjects,
      datasets: [
        {
          label: "Scores",
          data: scores,
          backgroundColor: "#4dabf7",
          borderRadius: 6
        },
        {
          type: "line",
          label: "Performance Trend",
          data: scores,
          borderColor: "#ffc300",
          borderWidth: 2,
          fill: false,
          tension: 0.3
        }
      ]
    },
    options: { responsive: true }
  });

   // Modal handling
  const modal = document.getElementById("courseModal");
  const closeBtn = document.querySelector(".close-btn");
  const modalCourse = document.getElementById("modalCourse");
  const courseRemarks = document.getElementById("courseRemarks");
  let courseChart;

  document.querySelectorAll(".results-table tbody tr").forEach(row => {
    row.addEventListener("click", () => {
      let index = row.getAttribute("data-index");
      modalCourse.innerText = subjects[index] + " - Detailed View";
      courseRemarks.innerText = getGrade(scores[index]).remark;

      // Destroy previous chart if exists
      if (courseChart) courseChart.destroy();

      // Mini chart for the subject
      const ctx2 = document.getElementById("courseChart").getContext("2d");
      courseChart = new Chart(ctx2, {
        type: "doughnut",
        data: {
          labels: ["Score", "Remaining"],
          datasets: [{
            data: [scores[index], 100 - scores[index]],
            backgroundColor: ["#4dabf7", "#ddd"]
          }]
        },
        options: { responsive: true, cutout: "70%" }
      });

      modal.style.display = "flex";
    });
  });

  // Close modal
  closeBtn.addEventListener("click", () => modal.style.display = "none");
  window.addEventListener("click", e => { if (e.target == modal) modal.style.display = "none"; });

// payments section

// Payment Modal
const openPaymentModal = document.getElementById("openPaymentModal");
const paymentModal = document.getElementById("paymentModal");
const closePaymentModal = document.getElementById("closePaymentModal");
const paymentForm = document.querySelector(".payment-form");
const paymentTableBody = document.querySelector(".payment-history tbody");

openPaymentModal.addEventListener("click", () => {
  paymentModal.style.display = "flex";
});

closePaymentModal.addEventListener("click", () => {
  paymentModal.style.display = "none";
});

window.addEventListener("click", (e) => {
  if (e.target == paymentModal) {
    paymentModal.style.display = "none";
  }
});

// Generate fake reference
function generateRef() {
  return "REF" + Math.floor(Math.random() * 100000);
}

// Handle Payment Submit
paymentForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const amount = document.getElementById("amount").value;
  const method = document.getElementById("method").value;

  if (!amount || !method) {
    alert("⚠️ Please fill all fields.");
    return;
  }

  const today = new Date().toISOString().split("T")[0]; // YYYY-MM-DD
  const ref = generateRef();

  // Add new row to table
  const newRow = `
    <tr>
      <td>${today}</td>
      <td>${ref}</td>
      <td>${method.charAt(0).toUpperCase() + method.slice(1)}</td>
      <td>₦${parseInt(amount).toLocaleString()}</td>
      <td style="color: orange; font-weight: bold;">Pending</td>
    </tr>
  `;

  paymentTableBody.insertAdjacentHTML("beforeend", newRow);

  alert("✅ Payment request submitted. Status: Pending");

  // Reset form + close modal
  paymentForm.reset();
  paymentModal.style.display = "none";
});

//student section

  document.querySelectorAll('.dropdown-toggle').forEach(toggle => {
    toggle.addEventListener('click', function(e) {
      e.preventDefault();
      this.parentElement.classList.toggle('open');
    });
  });
// logout warning
function confirmLogout(event) {
  let confirmed = confirm("Are you sure you want to logout?");
  if (!confirmed) {
    event.preventDefault();
    return false;
  }
  return true;

}
// End of student-dashboard


