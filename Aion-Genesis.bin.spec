# ==========================================
# AION NATIVE BINARY SPECIFICATION (GENESIS)
# Purpose: Direct CPU Boot & Hardware Control
# ==========================================

[BINARY_HEADER]
MAGIC_NUMBER: 0x41494F4E (A-I-O-N in Hex)
ENTRY_POINT:  0x0001 (Start from main unit)
ARCH:         NATIVE_ARM_X86_HYBRID

[HARDWARE_INITIALIZATION]
0x100: INIT_AI_CORE        // AI প্রসেসরকে জাগিয়ে তোলা
0x101: ENABLE_DNA_READER   // ফিঙ্গারপ্রিন্ট সেন্সরকে পাওয়ার দেওয়া
0x102: WAKE_DISPLAY_BUS    // গ্রাফিক্স ড্রাইভারে সরাসরি সংযোগ

[RUNTIME_POLICY]
# কোম্পানিগুলোর সাথে চুক্তি বাতিল হলে তাদের সার্ভিস ব্লক করার লজিক
POLICY_KILL_SWITCH: ENABLED 
SECURE_FINGERPRINT: SEPARATE_FROM_OS

[EXECUTION_ORDER]
1. EXEC Aion-Linker.native
2. SYNC core_boot.aion
3. MONITOR REG_S (Sensor Data)
4. IF AUTH_FAIL -> HALT_ALL
