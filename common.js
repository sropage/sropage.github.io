document.addEventListener('DOMContentLoaded', function() {
    // 点击触发下拉菜单
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
    
    dropdownToggles.forEach(toggle => {
      toggle.addEventListener('click', function(e) {
        e.stopPropagation();
        const dropdown = this.closest('.dropdown');
        const isActive = dropdown.classList.contains('active');
        
        // 关闭所有其他下拉菜单
        document.querySelectorAll('.dropdown').forEach(d => {
          if (d !== dropdown) d.classList.remove('active');
        });
        
        // 切换当前下拉菜单
        dropdown.classList.toggle('active', !isActive);
      });
    });
    
    // 点击页面其他位置关闭下拉菜单
    document.addEventListener('click', function() {
      document.querySelectorAll('.dropdown').forEach(d => {
        d.classList.remove('active');
      });
    });
  });


