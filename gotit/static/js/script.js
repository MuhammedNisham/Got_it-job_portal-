// javascript for search button in jobspage
document.addEventListener("DOMContentLoaded", function() {
  const searchInput = document.getElementById('jobSearchInput');
  const searchBtn = document.getElementById('jobSearchBtn');
  const jobItems = document.querySelectorAll('.job-list-item');

  function filterJobs() {
    const query = searchInput.value.trim().toLowerCase();
    jobItems.forEach(item => {
      // Collect all searchable fields
      const text = (
        item.dataset.company + " " +
        item.dataset.role + " " +
        item.dataset.location + " " +
        item.dataset.salary + " " +
        item.dataset.description
      );
      if (text.includes(query)) {
        item.style.display = "";
      } else {
        item.style.display = "none";
      }
    });
  }

  // Filter as user types
  searchInput.addEventListener('input', filterJobs);
  // Filter on button click
  searchBtn.addEventListener('click', filterJobs);
});

// javascript for applied job
document.addEventListener('DOMContentLoaded', function() {
    // Notification toggle
    const notifBtn = document.getElementById('notifBtn');
    const notifications = document.getElementById('notifications');
    notifBtn.addEventListener('click', function() {
        notifications.style.display = (notifications.style.display === 'none') ? 'block' : 'none';
    });

    // Applied Jobs toggle
    const showBtn = document.getElementById('showAppliedBtn');
    const cards = document.getElementById('appliedJobsCards');
    let shown = false;
    showBtn.addEventListener('click', function() {
        shown = !shown;
        cards.style.display = shown ? 'block' : 'none';
        showBtn.textContent = shown ? 'Hide Applied Jobs' : 'Show Applied Jobs';
    });
});

// javascript for jobcard posted-time
function timeAgoShort(dateString) {
    const now = new Date();
    const posted = new Date(dateString);
    const diffMs = now - posted;
    const diffSec = Math.floor(diffMs / 1000);
    const diffMin = Math.floor(diffSec / 60);
    const diffHr = Math.floor(diffMin / 60);
    const diffDay = Math.floor(diffHr / 24);

    if (diffDay >= 1) {
        return diffDay + 'd';
    } else if (diffHr >= 1) {
        return diffHr + 'h';
    } else if (diffMin >= 1) {
        return diffMin + 'm';
    } else {
        return 'Just now';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Job list cards
    document.querySelectorAll('.job-list-item').forEach(function(item) {
        var posted = item.getAttribute('data-posted');
        var timeElem = item.querySelector('.posted-time');
        if (posted && timeElem) {
            timeElem.textContent = timeAgoShort(posted);
        }
    });
    // Job details card
    var detailElem = document.querySelector('.posted-time-detail');
    if (detailElem) {
        var posted = detailElem.getAttribute('data-posted');
        if (posted) {
            detailElem.textContent = timeAgoShort(posted);
        }
    }
});

// javascript for for adding our systems local time in community Chat 
document.addEventListener('DOMContentLoaded', function() {
    // For all message timestamps, replace with current system time
    var now = new Date();
    var nowStr = now.toLocaleString(); // Adjust formatting as needed

    document.querySelectorAll('.message-timestamp').forEach(function(elem) {
        elem.textContent = '(' + nowStr + ')';
    });
});



