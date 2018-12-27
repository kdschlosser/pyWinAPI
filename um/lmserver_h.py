import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMSERVER_ = None


class _SERVER_INFO_100(ctypes.Structure):
    pass


SERVER_INFO_100 = _SERVER_INFO_100
PSERVER_INFO_100 = POINTER(_SERVER_INFO_100)
LPSERVER_INFO_100 = POINTER(_SERVER_INFO_100)


class _SERVER_INFO_101(ctypes.Structure):
    pass


SERVER_INFO_101 = _SERVER_INFO_101
PSERVER_INFO_101 = POINTER(_SERVER_INFO_101)
LPSERVER_INFO_101 = POINTER(_SERVER_INFO_101)


class _SERVER_INFO_102(ctypes.Structure):
    pass


SERVER_INFO_102 = _SERVER_INFO_102
PSERVER_INFO_102 = POINTER(_SERVER_INFO_102)
LPSERVER_INFO_102 = POINTER(_SERVER_INFO_102)


class _SERVER_INFO_103(ctypes.Structure):
    pass


SERVER_INFO_103 = _SERVER_INFO_103
PSERVER_INFO_103 = POINTER(_SERVER_INFO_103)
LPSERVER_INFO_103 = POINTER(_SERVER_INFO_103)


class _SERVER_INFO_402(ctypes.Structure):
    pass


SERVER_INFO_402 = _SERVER_INFO_402
PSERVER_INFO_402 = POINTER(_SERVER_INFO_402)
LPSERVER_INFO_402 = POINTER(_SERVER_INFO_402)


class _SERVER_INFO_403(ctypes.Structure):
    pass


SERVER_INFO_403 = _SERVER_INFO_403
PSERVER_INFO_403 = POINTER(_SERVER_INFO_403)
LPSERVER_INFO_403 = POINTER(_SERVER_INFO_403)


class _SERVER_INFO_502(ctypes.Structure):
    pass


SERVER_INFO_502 = _SERVER_INFO_502
PSERVER_INFO_502 = POINTER(_SERVER_INFO_502)
LPSERVER_INFO_502 = POINTER(_SERVER_INFO_502)


class _SERVER_INFO_503(ctypes.Structure):
    pass


SERVER_INFO_503 = _SERVER_INFO_503
PSERVER_INFO_503 = POINTER(_SERVER_INFO_503)
LPSERVER_INFO_503 = POINTER(_SERVER_INFO_503)


class _SERVER_INFO_599(ctypes.Structure):
    pass


SERVER_INFO_599 = _SERVER_INFO_599
PSERVER_INFO_599 = POINTER(_SERVER_INFO_599)
LPSERVER_INFO_599 = POINTER(_SERVER_INFO_599)


class _SERVER_INFO_598(ctypes.Structure):
    pass


SERVER_INFO_598 = _SERVER_INFO_598
PSERVER_INFO_598 = POINTER(_SERVER_INFO_598)
LPSERVER_INFO_598 = POINTER(_SERVER_INFO_598)


class _SERVER_INFO_1005(ctypes.Structure):
    pass


SERVER_INFO_1005 = _SERVER_INFO_1005
PSERVER_INFO_1005 = POINTER(_SERVER_INFO_1005)
LPSERVER_INFO_1005 = POINTER(_SERVER_INFO_1005)


class _SERVER_INFO_1107(ctypes.Structure):
    pass


SERVER_INFO_1107 = _SERVER_INFO_1107
PSERVER_INFO_1107 = POINTER(_SERVER_INFO_1107)
LPSERVER_INFO_1107 = POINTER(_SERVER_INFO_1107)


class _SERVER_INFO_1010(ctypes.Structure):
    pass


SERVER_INFO_1010 = _SERVER_INFO_1010
PSERVER_INFO_1010 = POINTER(_SERVER_INFO_1010)
LPSERVER_INFO_1010 = POINTER(_SERVER_INFO_1010)


class _SERVER_INFO_1016(ctypes.Structure):
    pass


SERVER_INFO_1016 = _SERVER_INFO_1016
PSERVER_INFO_1016 = POINTER(_SERVER_INFO_1016)
LPSERVER_INFO_1016 = POINTER(_SERVER_INFO_1016)


class _SERVER_INFO_1017(ctypes.Structure):
    pass


SERVER_INFO_1017 = _SERVER_INFO_1017
PSERVER_INFO_1017 = POINTER(_SERVER_INFO_1017)
LPSERVER_INFO_1017 = POINTER(_SERVER_INFO_1017)


class _SERVER_INFO_1018(ctypes.Structure):
    pass


SERVER_INFO_1018 = _SERVER_INFO_1018
PSERVER_INFO_1018 = POINTER(_SERVER_INFO_1018)
LPSERVER_INFO_1018 = POINTER(_SERVER_INFO_1018)


class _SERVER_INFO_1501(ctypes.Structure):
    pass


SERVER_INFO_1501 = _SERVER_INFO_1501
PSERVER_INFO_1501 = POINTER(_SERVER_INFO_1501)
LPSERVER_INFO_1501 = POINTER(_SERVER_INFO_1501)


class _SERVER_INFO_1502(ctypes.Structure):
    pass


SERVER_INFO_1502 = _SERVER_INFO_1502
PSERVER_INFO_1502 = POINTER(_SERVER_INFO_1502)
LPSERVER_INFO_1502 = POINTER(_SERVER_INFO_1502)


class _SERVER_INFO_1503(ctypes.Structure):
    pass


SERVER_INFO_1503 = _SERVER_INFO_1503
PSERVER_INFO_1503 = POINTER(_SERVER_INFO_1503)
LPSERVER_INFO_1503 = POINTER(_SERVER_INFO_1503)


class _SERVER_INFO_1506(ctypes.Structure):
    pass


SERVER_INFO_1506 = _SERVER_INFO_1506
PSERVER_INFO_1506 = POINTER(_SERVER_INFO_1506)
LPSERVER_INFO_1506 = POINTER(_SERVER_INFO_1506)


class _SERVER_INFO_1509(ctypes.Structure):
    pass


SERVER_INFO_1509 = _SERVER_INFO_1509
PSERVER_INFO_1509 = POINTER(_SERVER_INFO_1509)
LPSERVER_INFO_1509 = POINTER(_SERVER_INFO_1509)


class _SERVER_INFO_1510(ctypes.Structure):
    pass


SERVER_INFO_1510 = _SERVER_INFO_1510
PSERVER_INFO_1510 = POINTER(_SERVER_INFO_1510)
LPSERVER_INFO_1510 = POINTER(_SERVER_INFO_1510)


class _SERVER_INFO_1511(ctypes.Structure):
    pass


SERVER_INFO_1511 = _SERVER_INFO_1511
PSERVER_INFO_1511 = POINTER(_SERVER_INFO_1511)
LPSERVER_INFO_1511 = POINTER(_SERVER_INFO_1511)


class _SERVER_INFO_1512(ctypes.Structure):
    pass


SERVER_INFO_1512 = _SERVER_INFO_1512
PSERVER_INFO_1512 = POINTER(_SERVER_INFO_1512)
LPSERVER_INFO_1512 = POINTER(_SERVER_INFO_1512)


class _SERVER_INFO_1513(ctypes.Structure):
    pass


SERVER_INFO_1513 = _SERVER_INFO_1513
PSERVER_INFO_1513 = POINTER(_SERVER_INFO_1513)
LPSERVER_INFO_1513 = POINTER(_SERVER_INFO_1513)


class _SERVER_INFO_1514(ctypes.Structure):
    pass


SERVER_INFO_1514 = _SERVER_INFO_1514
PSERVER_INFO_1514 = POINTER(_SERVER_INFO_1514)
LPSERVER_INFO_1514 = POINTER(_SERVER_INFO_1514)


class _SERVER_INFO_1515(ctypes.Structure):
    pass


SERVER_INFO_1515 = _SERVER_INFO_1515
PSERVER_INFO_1515 = POINTER(_SERVER_INFO_1515)
LPSERVER_INFO_1515 = POINTER(_SERVER_INFO_1515)


class _SERVER_INFO_1516(ctypes.Structure):
    pass


SERVER_INFO_1516 = _SERVER_INFO_1516
PSERVER_INFO_1516 = POINTER(_SERVER_INFO_1516)
LPSERVER_INFO_1516 = POINTER(_SERVER_INFO_1516)


class _SERVER_INFO_1518(ctypes.Structure):
    pass


SERVER_INFO_1518 = _SERVER_INFO_1518
PSERVER_INFO_1518 = POINTER(_SERVER_INFO_1518)
LPSERVER_INFO_1518 = POINTER(_SERVER_INFO_1518)


class _SERVER_INFO_1520(ctypes.Structure):
    pass


SERVER_INFO_1520 = _SERVER_INFO_1520
PSERVER_INFO_1520 = POINTER(_SERVER_INFO_1520)
LPSERVER_INFO_1520 = POINTER(_SERVER_INFO_1520)


class _SERVER_INFO_1521(ctypes.Structure):
    pass


SERVER_INFO_1521 = _SERVER_INFO_1521
PSERVER_INFO_1521 = POINTER(_SERVER_INFO_1521)
LPSERVER_INFO_1521 = POINTER(_SERVER_INFO_1521)


class _SERVER_INFO_1522(ctypes.Structure):
    pass


SERVER_INFO_1522 = _SERVER_INFO_1522
PSERVER_INFO_1522 = POINTER(_SERVER_INFO_1522)
LPSERVER_INFO_1522 = POINTER(_SERVER_INFO_1522)


class _SERVER_INFO_1523(ctypes.Structure):
    pass


SERVER_INFO_1523 = _SERVER_INFO_1523
PSERVER_INFO_1523 = POINTER(_SERVER_INFO_1523)
LPSERVER_INFO_1523 = POINTER(_SERVER_INFO_1523)


class _SERVER_INFO_1524(ctypes.Structure):
    pass


SERVER_INFO_1524 = _SERVER_INFO_1524
PSERVER_INFO_1524 = POINTER(_SERVER_INFO_1524)
LPSERVER_INFO_1524 = POINTER(_SERVER_INFO_1524)


class _SERVER_INFO_1525(ctypes.Structure):
    pass


SERVER_INFO_1525 = _SERVER_INFO_1525
PSERVER_INFO_1525 = POINTER(_SERVER_INFO_1525)
LPSERVER_INFO_1525 = POINTER(_SERVER_INFO_1525)


class _SERVER_INFO_1528(ctypes.Structure):
    pass


SERVER_INFO_1528 = _SERVER_INFO_1528
PSERVER_INFO_1528 = POINTER(_SERVER_INFO_1528)
LPSERVER_INFO_1528 = POINTER(_SERVER_INFO_1528)


class _SERVER_INFO_1529(ctypes.Structure):
    pass


SERVER_INFO_1529 = _SERVER_INFO_1529
PSERVER_INFO_1529 = POINTER(_SERVER_INFO_1529)
LPSERVER_INFO_1529 = POINTER(_SERVER_INFO_1529)


class _SERVER_INFO_1530(ctypes.Structure):
    pass


SERVER_INFO_1530 = _SERVER_INFO_1530
PSERVER_INFO_1530 = POINTER(_SERVER_INFO_1530)
LPSERVER_INFO_1530 = POINTER(_SERVER_INFO_1530)


class _SERVER_INFO_1533(ctypes.Structure):
    pass


SERVER_INFO_1533 = _SERVER_INFO_1533
PSERVER_INFO_1533 = POINTER(_SERVER_INFO_1533)
LPSERVER_INFO_1533 = POINTER(_SERVER_INFO_1533)


class _SERVER_INFO_1534(ctypes.Structure):
    pass


SERVER_INFO_1534 = _SERVER_INFO_1534
PSERVER_INFO_1534 = POINTER(_SERVER_INFO_1534)
LPSERVER_INFO_1534 = POINTER(_SERVER_INFO_1534)


class _SERVER_INFO_1535(ctypes.Structure):
    pass


SERVER_INFO_1535 = _SERVER_INFO_1535
PSERVER_INFO_1535 = POINTER(_SERVER_INFO_1535)
LPSERVER_INFO_1535 = POINTER(_SERVER_INFO_1535)


class _SERVER_INFO_1536(ctypes.Structure):
    pass


SERVER_INFO_1536 = _SERVER_INFO_1536
PSERVER_INFO_1536 = POINTER(_SERVER_INFO_1536)
LPSERVER_INFO_1536 = POINTER(_SERVER_INFO_1536)


class _SERVER_INFO_1537(ctypes.Structure):
    pass


SERVER_INFO_1537 = _SERVER_INFO_1537
PSERVER_INFO_1537 = POINTER(_SERVER_INFO_1537)
LPSERVER_INFO_1537 = POINTER(_SERVER_INFO_1537)


class _SERVER_INFO_1538(ctypes.Structure):
    pass


SERVER_INFO_1538 = _SERVER_INFO_1538
PSERVER_INFO_1538 = POINTER(_SERVER_INFO_1538)
LPSERVER_INFO_1538 = POINTER(_SERVER_INFO_1538)


class _SERVER_INFO_1539(ctypes.Structure):
    pass


SERVER_INFO_1539 = _SERVER_INFO_1539
PSERVER_INFO_1539 = POINTER(_SERVER_INFO_1539)
LPSERVER_INFO_1539 = POINTER(_SERVER_INFO_1539)


class _SERVER_INFO_1540(ctypes.Structure):
    pass


SERVER_INFO_1540 = _SERVER_INFO_1540
PSERVER_INFO_1540 = POINTER(_SERVER_INFO_1540)
LPSERVER_INFO_1540 = POINTER(_SERVER_INFO_1540)


class _SERVER_INFO_1541(ctypes.Structure):
    pass


SERVER_INFO_1541 = _SERVER_INFO_1541
PSERVER_INFO_1541 = POINTER(_SERVER_INFO_1541)
LPSERVER_INFO_1541 = POINTER(_SERVER_INFO_1541)


class _SERVER_INFO_1542(ctypes.Structure):
    pass


SERVER_INFO_1542 = _SERVER_INFO_1542
PSERVER_INFO_1542 = POINTER(_SERVER_INFO_1542)
LPSERVER_INFO_1542 = POINTER(_SERVER_INFO_1542)


class _SERVER_INFO_1543(ctypes.Structure):
    pass


SERVER_INFO_1543 = _SERVER_INFO_1543
PSERVER_INFO_1543 = POINTER(_SERVER_INFO_1543)
LPSERVER_INFO_1543 = POINTER(_SERVER_INFO_1543)


class _SERVER_INFO_1544(ctypes.Structure):
    pass


SERVER_INFO_1544 = _SERVER_INFO_1544
PSERVER_INFO_1544 = POINTER(_SERVER_INFO_1544)
LPSERVER_INFO_1544 = POINTER(_SERVER_INFO_1544)


class _SERVER_INFO_1545(ctypes.Structure):
    pass


SERVER_INFO_1545 = _SERVER_INFO_1545
PSERVER_INFO_1545 = POINTER(_SERVER_INFO_1545)
LPSERVER_INFO_1545 = POINTER(_SERVER_INFO_1545)


class _SERVER_INFO_1546(ctypes.Structure):
    pass


SERVER_INFO_1546 = _SERVER_INFO_1546
PSERVER_INFO_1546 = POINTER(_SERVER_INFO_1546)
LPSERVER_INFO_1546 = POINTER(_SERVER_INFO_1546)


class _SERVER_INFO_1547(ctypes.Structure):
    pass


SERVER_INFO_1547 = _SERVER_INFO_1547
PSERVER_INFO_1547 = POINTER(_SERVER_INFO_1547)
LPSERVER_INFO_1547 = POINTER(_SERVER_INFO_1547)


class _SERVER_INFO_1548(ctypes.Structure):
    pass


SERVER_INFO_1548 = _SERVER_INFO_1548
PSERVER_INFO_1548 = POINTER(_SERVER_INFO_1548)
LPSERVER_INFO_1548 = POINTER(_SERVER_INFO_1548)


class _SERVER_INFO_1549(ctypes.Structure):
    pass


SERVER_INFO_1549 = _SERVER_INFO_1549
PSERVER_INFO_1549 = POINTER(_SERVER_INFO_1549)
LPSERVER_INFO_1549 = POINTER(_SERVER_INFO_1549)


class _SERVER_INFO_1550(ctypes.Structure):
    pass


SERVER_INFO_1550 = _SERVER_INFO_1550
PSERVER_INFO_1550 = POINTER(_SERVER_INFO_1550)
LPSERVER_INFO_1550 = POINTER(_SERVER_INFO_1550)


class _SERVER_INFO_1552(ctypes.Structure):
    pass


SERVER_INFO_1552 = _SERVER_INFO_1552
PSERVER_INFO_1552 = POINTER(_SERVER_INFO_1552)
LPSERVER_INFO_1552 = POINTER(_SERVER_INFO_1552)


class _SERVER_INFO_1553(ctypes.Structure):
    pass


SERVER_INFO_1553 = _SERVER_INFO_1553
PSERVER_INFO_1553 = POINTER(_SERVER_INFO_1553)
LPSERVER_INFO_1553 = POINTER(_SERVER_INFO_1553)


class _SERVER_INFO_1554(ctypes.Structure):
    pass


SERVER_INFO_1554 = _SERVER_INFO_1554
PSERVER_INFO_1554 = POINTER(_SERVER_INFO_1554)
LPSERVER_INFO_1554 = POINTER(_SERVER_INFO_1554)


class _SERVER_INFO_1555(ctypes.Structure):
    pass


SERVER_INFO_1555 = _SERVER_INFO_1555
PSERVER_INFO_1555 = POINTER(_SERVER_INFO_1555)
LPSERVER_INFO_1555 = POINTER(_SERVER_INFO_1555)


class _SERVER_INFO_1556(ctypes.Structure):
    pass


SERVER_INFO_1556 = _SERVER_INFO_1556
PSERVER_INFO_1556 = POINTER(_SERVER_INFO_1556)
LPSERVER_INFO_1556 = POINTER(_SERVER_INFO_1556)


class _SERVER_INFO_1557(ctypes.Structure):
    pass


SERVER_INFO_1557 = _SERVER_INFO_1557
PSERVER_INFO_1557 = POINTER(_SERVER_INFO_1557)
LPSERVER_INFO_1557 = POINTER(_SERVER_INFO_1557)


class _SERVER_INFO_1560(ctypes.Structure):
    pass


SERVER_INFO_1560 = _SERVER_INFO_1560
PSERVER_INFO_1560 = POINTER(_SERVER_INFO_1560)
LPSERVER_INFO_1560 = POINTER(_SERVER_INFO_1560)


class _SERVER_INFO_1561(ctypes.Structure):
    pass


SERVER_INFO_1561 = _SERVER_INFO_1561
PSERVER_INFO_1561 = POINTER(_SERVER_INFO_1561)
LPSERVER_INFO_1561 = POINTER(_SERVER_INFO_1561)


class _SERVER_INFO_1562(ctypes.Structure):
    pass


SERVER_INFO_1562 = _SERVER_INFO_1562
PSERVER_INFO_1562 = POINTER(_SERVER_INFO_1562)
LPSERVER_INFO_1562 = POINTER(_SERVER_INFO_1562)


class _SERVER_INFO_1563(ctypes.Structure):
    pass


SERVER_INFO_1563 = _SERVER_INFO_1563
PSERVER_INFO_1563 = POINTER(_SERVER_INFO_1563)
LPSERVER_INFO_1563 = POINTER(_SERVER_INFO_1563)


class _SERVER_INFO_1564(ctypes.Structure):
    pass


SERVER_INFO_1564 = _SERVER_INFO_1564
PSERVER_INFO_1564 = POINTER(_SERVER_INFO_1564)
LPSERVER_INFO_1564 = POINTER(_SERVER_INFO_1564)


class _SERVER_INFO_1565(ctypes.Structure):
    pass


SERVER_INFO_1565 = _SERVER_INFO_1565
PSERVER_INFO_1565 = POINTER(_SERVER_INFO_1565)
LPSERVER_INFO_1565 = POINTER(_SERVER_INFO_1565)


class _SERVER_INFO_1566(ctypes.Structure):
    pass


SERVER_INFO_1566 = _SERVER_INFO_1566
PSERVER_INFO_1566 = POINTER(_SERVER_INFO_1566)
LPSERVER_INFO_1566 = POINTER(_SERVER_INFO_1566)


class _SERVER_INFO_1567(ctypes.Structure):
    pass


SERVER_INFO_1567 = _SERVER_INFO_1567
PSERVER_INFO_1567 = POINTER(_SERVER_INFO_1567)
LPSERVER_INFO_1567 = POINTER(_SERVER_INFO_1567)


class _SERVER_INFO_1568(ctypes.Structure):
    pass


SERVER_INFO_1568 = _SERVER_INFO_1568
PSERVER_INFO_1568 = POINTER(_SERVER_INFO_1568)
LPSERVER_INFO_1568 = POINTER(_SERVER_INFO_1568)


class _SERVER_INFO_1569(ctypes.Structure):
    pass


SERVER_INFO_1569 = _SERVER_INFO_1569
PSERVER_INFO_1569 = POINTER(_SERVER_INFO_1569)
LPSERVER_INFO_1569 = POINTER(_SERVER_INFO_1569)


class _SERVER_INFO_1570(ctypes.Structure):
    pass


SERVER_INFO_1570 = _SERVER_INFO_1570
PSERVER_INFO_1570 = POINTER(_SERVER_INFO_1570)
LPSERVER_INFO_1570 = POINTER(_SERVER_INFO_1570)


class _SERVER_INFO_1571(ctypes.Structure):
    pass


SERVER_INFO_1571 = _SERVER_INFO_1571
PSERVER_INFO_1571 = POINTER(_SERVER_INFO_1571)
LPSERVER_INFO_1571 = POINTER(_SERVER_INFO_1571)


class _SERVER_INFO_1572(ctypes.Structure):
    pass


SERVER_INFO_1572 = _SERVER_INFO_1572
PSERVER_INFO_1572 = POINTER(_SERVER_INFO_1572)
LPSERVER_INFO_1572 = POINTER(_SERVER_INFO_1572)


class _SERVER_INFO_1573(ctypes.Structure):
    pass


SERVER_INFO_1573 = _SERVER_INFO_1573
PSERVER_INFO_1573 = POINTER(_SERVER_INFO_1573)
LPSERVER_INFO_1573 = POINTER(_SERVER_INFO_1573)


class _SERVER_INFO_1574(ctypes.Structure):
    pass


SERVER_INFO_1574 = _SERVER_INFO_1574
PSERVER_INFO_1574 = POINTER(_SERVER_INFO_1574)
LPSERVER_INFO_1574 = POINTER(_SERVER_INFO_1574)


class _SERVER_INFO_1575(ctypes.Structure):
    pass


SERVER_INFO_1575 = _SERVER_INFO_1575
PSERVER_INFO_1575 = POINTER(_SERVER_INFO_1575)
LPSERVER_INFO_1575 = POINTER(_SERVER_INFO_1575)


class _SERVER_INFO_1576(ctypes.Structure):
    pass


SERVER_INFO_1576 = _SERVER_INFO_1576
PSERVER_INFO_1576 = POINTER(_SERVER_INFO_1576)
LPSERVER_INFO_1576 = POINTER(_SERVER_INFO_1576)


class _SERVER_INFO_1577(ctypes.Structure):
    pass


SERVER_INFO_1577 = _SERVER_INFO_1577
PSERVER_INFO_1577 = POINTER(_SERVER_INFO_1577)
LPSERVER_INFO_1577 = POINTER(_SERVER_INFO_1577)


class _SERVER_INFO_1578(ctypes.Structure):
    pass


SERVER_INFO_1578 = _SERVER_INFO_1578
PSERVER_INFO_1578 = POINTER(_SERVER_INFO_1578)
LPSERVER_INFO_1578 = POINTER(_SERVER_INFO_1578)


class _SERVER_INFO_1579(ctypes.Structure):
    pass


SERVER_INFO_1579 = _SERVER_INFO_1579
PSERVER_INFO_1579 = POINTER(_SERVER_INFO_1579)
LPSERVER_INFO_1579 = POINTER(_SERVER_INFO_1579)


class _SERVER_INFO_1580(ctypes.Structure):
    pass


SERVER_INFO_1580 = _SERVER_INFO_1580
PSERVER_INFO_1580 = POINTER(_SERVER_INFO_1580)
LPSERVER_INFO_1580 = POINTER(_SERVER_INFO_1580)


class _SERVER_INFO_1581(ctypes.Structure):
    pass


SERVER_INFO_1581 = _SERVER_INFO_1581
PSERVER_INFO_1581 = POINTER(_SERVER_INFO_1581)
LPSERVER_INFO_1581 = POINTER(_SERVER_INFO_1581)


class _SERVER_INFO_1582(ctypes.Structure):
    pass


SERVER_INFO_1582 = _SERVER_INFO_1582
PSERVER_INFO_1582 = POINTER(_SERVER_INFO_1582)
LPSERVER_INFO_1582 = POINTER(_SERVER_INFO_1582)


class _SERVER_INFO_1583(ctypes.Structure):
    pass


SERVER_INFO_1583 = _SERVER_INFO_1583
PSERVER_INFO_1583 = POINTER(_SERVER_INFO_1583)
LPSERVER_INFO_1583 = POINTER(_SERVER_INFO_1583)


class _SERVER_INFO_1584(ctypes.Structure):
    pass


SERVER_INFO_1584 = _SERVER_INFO_1584
PSERVER_INFO_1584 = POINTER(_SERVER_INFO_1584)
LPSERVER_INFO_1584 = POINTER(_SERVER_INFO_1584)


class _SERVER_INFO_1585(ctypes.Structure):
    pass


SERVER_INFO_1585 = _SERVER_INFO_1585
PSERVER_INFO_1585 = POINTER(_SERVER_INFO_1585)
LPSERVER_INFO_1585 = POINTER(_SERVER_INFO_1585)


class _SERVER_INFO_1586(ctypes.Structure):
    pass


SERVER_INFO_1586 = _SERVER_INFO_1586
PSERVER_INFO_1586 = POINTER(_SERVER_INFO_1586)
LPSERVER_INFO_1586 = POINTER(_SERVER_INFO_1586)


class _SERVER_INFO_1587(ctypes.Structure):
    pass


SERVER_INFO_1587 = _SERVER_INFO_1587
PSERVER_INFO_1587 = POINTER(_SERVER_INFO_1587)
LPSERVER_INFO_1587 = POINTER(_SERVER_INFO_1587)


class _SERVER_INFO_1588(ctypes.Structure):
    pass


SERVER_INFO_1588 = _SERVER_INFO_1588
PSERVER_INFO_1588 = POINTER(_SERVER_INFO_1588)
LPSERVER_INFO_1588 = POINTER(_SERVER_INFO_1588)


class _SERVER_INFO_1590(ctypes.Structure):
    pass


SERVER_INFO_1590 = _SERVER_INFO_1590
PSERVER_INFO_1590 = POINTER(_SERVER_INFO_1590)
LPSERVER_INFO_1590 = POINTER(_SERVER_INFO_1590)


class _SERVER_INFO_1591(ctypes.Structure):
    pass


SERVER_INFO_1591 = _SERVER_INFO_1591
PSERVER_INFO_1591 = POINTER(_SERVER_INFO_1591)
LPSERVER_INFO_1591 = POINTER(_SERVER_INFO_1591)


class _SERVER_INFO_1592(ctypes.Structure):
    pass


SERVER_INFO_1592 = _SERVER_INFO_1592
PSERVER_INFO_1592 = POINTER(_SERVER_INFO_1592)
LPSERVER_INFO_1592 = POINTER(_SERVER_INFO_1592)


class _SERVER_INFO_1593(ctypes.Structure):
    pass


SERVER_INFO_1593 = _SERVER_INFO_1593
PSERVER_INFO_1593 = POINTER(_SERVER_INFO_1593)
LPSERVER_INFO_1593 = POINTER(_SERVER_INFO_1593)


class _SERVER_INFO_1594(ctypes.Structure):
    pass


SERVER_INFO_1594 = _SERVER_INFO_1594
PSERVER_INFO_1594 = POINTER(_SERVER_INFO_1594)
LPSERVER_INFO_1594 = POINTER(_SERVER_INFO_1594)


class _SERVER_INFO_1595(ctypes.Structure):
    pass


SERVER_INFO_1595 = _SERVER_INFO_1595
PSERVER_INFO_1595 = POINTER(_SERVER_INFO_1595)
LPSERVER_INFO_1595 = POINTER(_SERVER_INFO_1595)


class _SERVER_INFO_1596(ctypes.Structure):
    pass


SERVER_INFO_1596 = _SERVER_INFO_1596
PSERVER_INFO_1596 = POINTER(_SERVER_INFO_1596)
LPSERVER_INFO_1596 = POINTER(_SERVER_INFO_1596)


class _SERVER_INFO_1597(ctypes.Structure):
    pass


SERVER_INFO_1597 = _SERVER_INFO_1597
PSERVER_INFO_1597 = POINTER(_SERVER_INFO_1597)
LPSERVER_INFO_1597 = POINTER(_SERVER_INFO_1597)


class _SERVER_INFO_1598(ctypes.Structure):
    pass


SERVER_INFO_1598 = _SERVER_INFO_1598
PSERVER_INFO_1598 = POINTER(_SERVER_INFO_1598)
LPSERVER_INFO_1598 = POINTER(_SERVER_INFO_1598)


class _SERVER_INFO_1599(ctypes.Structure):
    pass


SERVER_INFO_1599 = _SERVER_INFO_1599
PSERVER_INFO_1599 = POINTER(_SERVER_INFO_1599)
LPSERVER_INFO_1599 = POINTER(_SERVER_INFO_1599)


class _SERVER_INFO_1600(ctypes.Structure):
    pass


SERVER_INFO_1600 = _SERVER_INFO_1600
PSERVER_INFO_1600 = POINTER(_SERVER_INFO_1600)
LPSERVER_INFO_1600 = POINTER(_SERVER_INFO_1600)


class _SERVER_INFO_1601(ctypes.Structure):
    pass


SERVER_INFO_1601 = _SERVER_INFO_1601
PSERVER_INFO_1601 = POINTER(_SERVER_INFO_1601)
LPSERVER_INFO_1601 = POINTER(_SERVER_INFO_1601)


class _SERVER_INFO_1602(ctypes.Structure):
    pass


SERVER_INFO_1602 = _SERVER_INFO_1602
PSERVER_INFO_1602 = POINTER(_SERVER_INFO_1602)
LPSERVER_INFO_1602 = POINTER(_SERVER_INFO_1602)


class _SERVER_TRANSPORT_INFO_0(ctypes.Structure):
    pass


SERVER_TRANSPORT_INFO_0 = _SERVER_TRANSPORT_INFO_0
PSERVER_TRANSPORT_INFO_0 = POINTER(_SERVER_TRANSPORT_INFO_0)
LPSERVER_TRANSPORT_INFO_0 = POINTER(_SERVER_TRANSPORT_INFO_0)


class _SERVER_TRANSPORT_INFO_1(ctypes.Structure):
    pass


SERVER_TRANSPORT_INFO_1 = _SERVER_TRANSPORT_INFO_1
PSERVER_TRANSPORT_INFO_1 = POINTER(_SERVER_TRANSPORT_INFO_1)
LPSERVER_TRANSPORT_INFO_1 = POINTER(_SERVER_TRANSPORT_INFO_1)


class _SERVER_TRANSPORT_INFO_2(ctypes.Structure):
    pass


SERVER_TRANSPORT_INFO_2 = _SERVER_TRANSPORT_INFO_2
PSERVER_TRANSPORT_INFO_2 = POINTER(_SERVER_TRANSPORT_INFO_2)
LPSERVER_TRANSPORT_INFO_2 = POINTER(_SERVER_TRANSPORT_INFO_2)


class _SERVER_TRANSPORT_INFO_3(ctypes.Structure):
    pass


SERVER_TRANSPORT_INFO_3 = _SERVER_TRANSPORT_INFO_3
PSERVER_TRANSPORT_INFO_3 = POINTER(_SERVER_TRANSPORT_INFO_3)
LPSERVER_TRANSPORT_INFO_3 = POINTER(_SERVER_TRANSPORT_INFO_3)


SERVER_TRANSPORT_INFO_0 = _SERVER_TRANSPORT_INFO_0
PSERVER_TRANSPORT_INFO_0 = POINTER(_SERVER_TRANSPORT_INFO_0)
LPSERVER_TRANSPORT_INFO_0 = POINTER(_SERVER_TRANSPORT_INFO_0)


SERVER_TRANSPORT_INFO_1 = _SERVER_TRANSPORT_INFO_1
PSERVER_TRANSPORT_INFO_1 = POINTER(_SERVER_TRANSPORT_INFO_1)
LPSERVER_TRANSPORT_INFO_1 = POINTER(_SERVER_TRANSPORT_INFO_1)


SERVER_TRANSPORT_INFO_2 = _SERVER_TRANSPORT_INFO_2
PSERVER_TRANSPORT_INFO_2 = POINTER(_SERVER_TRANSPORT_INFO_2)
LPSERVER_TRANSPORT_INFO_2 = POINTER(_SERVER_TRANSPORT_INFO_2)


SERVER_TRANSPORT_INFO_3 = _SERVER_TRANSPORT_INFO_3
PSERVER_TRANSPORT_INFO_3 = POINTER(_SERVER_TRANSPORT_INFO_3)
LPSERVER_TRANSPORT_INFO_3 = POINTER(_SERVER_TRANSPORT_INFO_3)


# /* + + BUILD VERSION: 0007 // INCREMENT THIS IF A CHANGE HAS GLOBAL EFFECTS
# Copyright (c) 1990-1999 Microsoft Corporation Module Name: lmserver.h
# Abstract: This file contains information about NetServer APIs. Function
# Prototypes Data Structures Definition of special values Environment: User
# Mode - Win32 Notes: You must include NETCONS.H before this file, since this
# file depends on values defined in NETCONS.H. --
if not defined(_LMSERVER_):
    _LMSERVER_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.shared.lmcons_h import *  # NOQA

    netapi32 = ctypes.windll.NETAPI32

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # SERVICE_STATUS_HANDLE
        from pyWinAPI.um.winsvc_h import * # NOQA
        if defined(__cplusplus):
            pass
        # END IF
    # END IF INAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # // Function Prototypes - SERVER

        # NET_API_STATUS NET_API_FUNCTION
        # NetServerEnum(
        # _In_opt_ IN  LMCSTR      servername OPTIONAL,
        # _In_ IN  DWORD       level,
        # _Outptr_result_buffer_(_Inexpressible_(entriesread)) OUT LPBYTE    *bufptr,
        # _In_ IN  DWORD       prefmaxlen,
        # _Out_ OUT LPDWORD     entriesread,
        # _Out_ OUT LPDWORD     totalentries,
        # _In_ IN  DWORD       servertype,
        # _In_opt_ IN  LMCSTR      domain OPTIONAL,
        # _Out_opt_ IN OUT LPDWORD  resume_handle OPTIONAL
        # );
        NetServerEnum = netapi32.NetServerEnum
        NetServerEnum.restype = NET_API_STATUS
        # NET_API_STATUS NET_API_FUNCTION
        # NetServerEnumEx(
        # _In_opt_ IN  LMCSTR      ServerName OPTIONAL,
        # _In_ IN  DWORD       Level,
        # _Outptr_result_buffer_(_Inexpressible_(*EntriesRead))
        # LPBYTE      *Bufptr,
        # _In_ IN  DWORD       PrefMaxlen,
        # _Out_ OUT LPDWORD     EntriesRead,
        # _Out_ OUT LPDWORD     totalentries,
        # _In_ IN  DWORD       servertype,
        # _In_opt_ IN  LMCSTR      domain OPTIONAL,
        # _In_opt_ IN  LMCSTR      FirstNameToReturn OPTIONAL
        # );
        NetServerEnumEx = netapi32.NetServerEnumEx
        NetServerEnumEx.restype = NET_API_STATUS
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(
        WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_
        # _Success_( return == 0 )
        # NET_API_STATUS NET_API_FUNCTION
        # NetServerGetInfo(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD level,
        # _When_( level == 100, _Outptr_result_bytebuffer_((ctypes.sizeof(SERVER_INFO_100)) )
        # _When_( level == 101, _Outptr_result_bytebuffer_((ctypes.sizeof(SERVER_INFO_101)) )
        # _When_( level == 102, _Outptr_result_bytebuffer_((ctypes.sizeof(SERVER_INFO_102)) )
        # LPBYTE *bufptr
        # );
        NetServerGetInfo = netapi32.NetServerGetInfo
        NetServerGetInfo.restype = NET_API_STATUS

        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetServerSetInfo(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD level,
        # _When_( level == 100, _In_reads_bytes_((ctypes.sizeof(SERVER_INFO_100)) )
        # _When_( level == 101, _In_reads_bytes_((ctypes.sizeof(SERVER_INFO_101)) )
        # _When_( level == 102, _In_reads_bytes_((ctypes.sizeof(SERVER_INFO_102)) )
        # _When_( level == 402, _In_reads_bytes_((ctypes.sizeof(SERVER_INFO_402)) )
        # _When_( level == 403, _In_reads_bytes_((ctypes.sizeof(SERVER_INFO_403)) )
        # _When_( level == 1005, _In_reads_bytes_((ctypes.sizeof(SERVER_INFO_1005)) )
        # _When_( level == 1010, _In_reads_bytes_((ctypes.sizeof(SERVER_INFO_1010)) )
        # _When_( level == 1016, _In_reads_bytes_((ctypes.sizeof(SERVER_INFO_1016)) )
        # _When_( level == 1017, _In_reads_bytes_((ctypes.sizeof(SERVER_INFO_1017)) )
        # _When_( level == 1018, _In_reads_bytes_((ctypes.sizeof(SERVER_INFO_1018)) )
        # LPBYTE  buf,
        # _Out_opt_ LPDWORD ParmError
        # );
        NetServerSetInfo = netapi32.NetServerSetInfo
        NetServerSetInfo.restype = NET_API_STATUS
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Temporary hack function.
        pass
        #  END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(
        WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_
        # _Success_( return == 0 or return == ERROR_MORE_DATA )
        # NET_API_STATUS NET_API_FUNCTION
        # NetServerDiskEnum(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD level,
        # _Outptr_result_bytebuffer_(((ctypes.sizeof(TCHAR) * 3 * (*entriesread)) + (ctypes.sizeof(TCHAR)) LPBYTE *bufptr,
        # _In_ DWORD prefmaxlen,
        # _Out_ LPDWORD entriesread,
        # _Out_ LPDWORD totalentries,
        # _Inout_opt_ LPDWORD resume_handle
        # );
        NetServerDiskEnum = netapi32.NetServerDiskEnum
        NetServerDiskEnum.restype = NET_API_STATUS

        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetServerComputerNameAdd(
        # _In_opt_ LMSTR ServerName,
        # _In_opt_ LMSTR EmulatedDomainName,
        # _In_ LMSTR EmulatedServerName
        # );
        NetServerComputerNameAdd = netapi32.NetServerComputerNameAdd
        NetServerComputerNameAdd.restype = NET_API_STATUS

        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetServerComputerNameDel(
        # _In_opt_ LMSTR ServerName,
        # _In_ LMSTR EmulatedServerName
        # );
        NetServerComputerNameDel = netapi32.NetServerComputerNameDel
        NetServerComputerNameDel.restype = NET_API_STATUS

        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetServerTransportAdd(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD level,
        # _In_reads_bytes_((ctypes.sizeof(SERVER_TRANSPORT_INFO_0)) LPBYTE bufptr
        # );
        NetServerTransportAdd = netapi32.NetServerTransportAdd
        NetServerTransportAdd.restype = NET_API_STATUS

        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetServerTransportAddEx(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD level,
        # _When_( level == 0, _In_reads_bytes_((ctypes.sizeof(SERVER_TRANSPORT_INFO_0)) )
        # _When_( level == 1, _In_reads_bytes_((ctypes.sizeof(SERVER_TRANSPORT_INFO_1)) )
        # _When_( level == 2, _In_reads_bytes_((ctypes.sizeof(SERVER_TRANSPORT_INFO_2)) )
        # _When_( level == 3, _In_reads_bytes_((ctypes.sizeof(SERVER_TRANSPORT_INFO_3)) )
        # LPBYTE bufptr
        # );
        NetServerTransportAddEx = netapi32.NetServerTransportAddEx
        NetServerTransportAddEx.restype = NET_API_STATUS
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(
        WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_
        # NET_API_STATUS NET_API_FUNCTION
        # NetServerTransportDel(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD level,
        # _When_( level == 0, _In_reads_bytes_((ctypes.sizeof(SERVER_TRANSPORT_INFO_0)) )
        # _When_( level == 1, _In_reads_bytes_((ctypes.sizeof(SERVER_TRANSPORT_INFO_1)) )
        # LPBYTE bufptr
        # );
        NetServerTransportDel = netapi32.NetServerTransportDel
        NetServerTransportDel.restype = NET_API_STATUS
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(
        WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_
        # _Success_( return == 0 or return == ERROR_MORE_DATA )
        # NET_API_STATUS NET_API_FUNCTION
        # NetServerTransportEnum(
        # _In_opt_ LMSTR servername,
        # _In_ DWORD level,
        # _When_( level == 0, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SERVER_TRANSPORT_INFO_0)) )
        # _When_( level == 1, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SERVER_TRANSPORT_INFO_1)) )
        # _When_( level == 2, _Outptr_result_bytebuffer_(*entriesread * (ctypes.sizeof(SERVER_TRANSPORT_INFO_2)) )
        # LPBYTE *bufptr,
        # _In_ DWORD prefmaxlen,
        # _Out_ LPDWORD entriesread,
        # _Out_ LPDWORD totalentries,
        # _Inout_opt_ LPDWORD resume_handle
        # );
        NetServerTransportEnum = netapi32.NetServerTransportEnum
        NetServerTransportEnum.restype = NET_API_STATUS
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # The following function can be called by Win NT services to
        # register
        # their service type. This function is exported from advapi32.dll.
        # Therefore, if this is the only function called by that service,
        # then
        # it is not necessary to link to netapi32.lib.
        # BOOL NET_API_FUNCTION
        # SetServiceBits(
        # IN SERVICE_STATUS_HANDLE    hServiceStatus,
        # IN DWORD                    dwServiceBits,
        # IN BOOL                     bSetBitsOn,
        # IN BOOL                     bUpdateImmediately
        # );
        SetServiceBits = advapi32.SetServiceBits
        SetServiceBits.restype = BOOL
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(
        WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # Data Structures - SERVER
        _SERVER_INFO_100._fields_ = [
            ('sv100_platform_id', DWORD),
            ('sv100_name', LMSTR),
        ]

        _SERVER_INFO_101._fields_ = [
            ('sv101_platform_id', DWORD),
            ('sv101_name', LMSTR),
            ('sv101_version_major', DWORD),
            ('sv101_version_minor', DWORD),
            ('sv101_type', DWORD),
            ('sv101_comment', LMSTR),
        ]

        _SERVER_INFO_102._fields_ = [
            ('sv102_platform_id', DWORD),
            ('sv102_name', LMSTR),
            ('sv102_version_major', DWORD),
            ('sv102_version_minor', DWORD),
            ('sv102_type', DWORD),
            ('sv102_comment', LMSTR),
            ('sv102_users', DWORD),
            ('sv102_disc', LONG),
            ('sv102_hidden', BOOL),
            ('sv102_announce', DWORD),
            ('sv102_anndelta', DWORD),
            ('sv102_licenses', DWORD),
            ('sv102_userpath', LMSTR),
        ]

        _SERVER_INFO_103._fields_ = [
            ('sv103_platform_id', DWORD),
            ('sv103_name', LMSTR),
            ('sv103_version_major', DWORD),
            ('sv103_version_minor', DWORD),
            ('sv103_type', DWORD),
            ('sv103_comment', LMSTR),
            ('sv103_users', DWORD),
            ('sv103_disc', LONG),
            ('sv103_hidden', BOOL),
            ('sv103_announce', DWORD),
            ('sv103_anndelta', DWORD),
            ('sv103_licenses', DWORD),
            ('sv103_userpath', LMSTR),
            ('sv103_capabilities', DWORD),
        ]

        _SERVER_INFO_402._fields_ = [
            ('sv402_ulist_mtime', DWORD),
            ('sv402_glist_mtime', DWORD),
            ('sv402_alist_mtime', DWORD),
            ('sv402_alerts', LMSTR),
            ('sv402_security', DWORD),
            ('sv402_numadmin', DWORD),
            ('sv402_lanmask', DWORD),
            ('sv402_guestacct', LMSTR),
            ('sv402_chdevs', DWORD),
            ('sv402_chdevq', DWORD),
            ('sv402_chdevjobs', DWORD),
            ('sv402_connections', DWORD),
            ('sv402_shares', DWORD),
            ('sv402_openfiles', DWORD),
            ('sv402_sessopens', DWORD),
            ('sv402_sessvcs', DWORD),
            ('sv402_sessreqs', DWORD),
            ('sv402_opensearch', DWORD),
            ('sv402_activelocks', DWORD),
            ('sv402_numreqbuf', DWORD),
            ('sv402_sizreqbuf', DWORD),
            ('sv402_numbigbuf', DWORD),
            ('sv402_numfiletasks', DWORD),
            ('sv402_alertsched', DWORD),
            ('sv402_erroralert', DWORD),
            ('sv402_logonalert', DWORD),
            ('sv402_accessalert', DWORD),
            ('sv402_diskalert', DWORD),
            ('sv402_netioalert', DWORD),
            ('sv402_maxauditsz', DWORD),
            ('sv402_srvheuristics', LMSTR),
        ]

        _SERVER_INFO_403._fields_ = [
            ('sv403_ulist_mtime', DWORD),
            ('sv403_glist_mtime', DWORD),
            ('sv403_alist_mtime', DWORD),
            ('sv403_alerts', LMSTR),
            ('sv403_security', DWORD),
            ('sv403_numadmin', DWORD),
            ('sv403_lanmask', DWORD),
            ('sv403_guestacct', LMSTR),
            ('sv403_chdevs', DWORD),
            ('sv403_chdevq', DWORD),
            ('sv403_chdevjobs', DWORD),
            ('sv403_connections', DWORD),
            ('sv403_shares', DWORD),
            ('sv403_openfiles', DWORD),
            ('sv403_sessopens', DWORD),
            ('sv403_sessvcs', DWORD),
            ('sv403_sessreqs', DWORD),
            ('sv403_opensearch', DWORD),
            ('sv403_activelocks', DWORD),
            ('sv403_numreqbuf', DWORD),
            ('sv403_sizreqbuf', DWORD),
            ('sv403_numbigbuf', DWORD),
            ('sv403_numfiletasks', DWORD),
            ('sv403_alertsched', DWORD),
            ('sv403_erroralert', DWORD),
            ('sv403_logonalert', DWORD),
            ('sv403_accessalert', DWORD),
            ('sv403_diskalert', DWORD),
            ('sv403_netioalert', DWORD),
            ('sv403_maxauditsz', DWORD),
            ('sv403_srvheuristics', LMSTR),
            ('sv403_auditedevents', DWORD),
            ('sv403_autoprofile', DWORD),
            ('sv403_autopath', LMSTR),
        ]

        _SERVER_INFO_502._fields_ = [
            ('sv502_sessopens', DWORD),
            ('sv502_sessvcs', DWORD),
            ('sv502_opensearch', DWORD),
            ('sv502_sizreqbuf', DWORD),
            ('sv502_initworkitems', DWORD),
            ('sv502_maxworkitems', DWORD),
            ('sv502_rawworkitems', DWORD),
            ('sv502_irpstacksize', DWORD),
            ('sv502_maxrawbuflen', DWORD),
            ('sv502_sessusers', DWORD),
            ('sv502_sessconns', DWORD),
            ('sv502_maxpagedmemoryusage', DWORD),
            ('sv502_maxnonpagedmemoryusage', DWORD),
            ('sv502_enablesoftcompat', BOOL),
            ('sv502_enableforcedlogoff', BOOL),
            ('sv502_timesource', BOOL),
            ('sv502_acceptdownlevelapis', BOOL),
            ('sv502_lmannounce', BOOL),
        ]

        _SERVER_INFO_503._fields_ = [
            ('sv503_sessopens', DWORD),
            ('sv503_sessvcs', DWORD),
            ('sv503_opensearch', DWORD),
            ('sv503_sizreqbuf', DWORD),
            ('sv503_initworkitems', DWORD),
            ('sv503_maxworkitems', DWORD),
            ('sv503_rawworkitems', DWORD),
            ('sv503_irpstacksize', DWORD),
            ('sv503_maxrawbuflen', DWORD),
            ('sv503_sessusers', DWORD),
            ('sv503_sessconns', DWORD),
            ('sv503_maxpagedmemoryusage', DWORD),
            ('sv503_maxnonpagedmemoryusage', DWORD),
            ('sv503_enablesoftcompat', BOOL),
            ('sv503_enableforcedlogoff', BOOL),
            ('sv503_timesource', BOOL),
            ('sv503_acceptdownlevelapis', BOOL),
            ('sv503_lmannounce', BOOL),
            ('sv503_domain', LMSTR),
            ('sv503_maxcopyreadlen', DWORD),
            ('sv503_maxcopywritelen', DWORD),
            ('sv503_minkeepsearch', DWORD),
            ('sv503_maxkeepsearch', DWORD),
            ('sv503_minkeepcomplsearch', DWORD),
            ('sv503_maxkeepcomplsearch', DWORD),
            ('sv503_threadcountadd', DWORD),
            ('sv503_numblockthreads', DWORD),
            ('sv503_scavtimeout', DWORD),
            ('sv503_minrcvqueue', DWORD),
            ('sv503_minfreeworkitems', DWORD),
            ('sv503_xactmemsize', DWORD),
            ('sv503_threadpriority', DWORD),
            ('sv503_maxmpxct', DWORD),
            ('sv503_oplockbreakwait', DWORD),
            ('sv503_oplockbreakresponsewait', DWORD),
            ('sv503_enableoplocks', BOOL),
            ('sv503_enableoplockforceclose', BOOL),
            ('sv503_enablefcbopens', BOOL),
            ('sv503_enableraw', BOOL),
            ('sv503_enablesharednetdrives', BOOL),
            ('sv503_minfreeconnections', DWORD),
            ('sv503_maxfreeconnections', DWORD),
        ]

        _SERVER_INFO_599._fields_ = [
            ('sv599_sessopens', DWORD),
            ('sv599_sessvcs', DWORD),
            ('sv599_opensearch', DWORD),
            ('sv599_sizreqbuf', DWORD),
            ('sv599_initworkitems', DWORD),
            ('sv599_maxworkitems', DWORD),
            ('sv599_rawworkitems', DWORD),
            ('sv599_irpstacksize', DWORD),
            ('sv599_maxrawbuflen', DWORD),
            ('sv599_sessusers', DWORD),
            ('sv599_sessconns', DWORD),
            ('sv599_maxpagedmemoryusage', DWORD),
            ('sv599_maxnonpagedmemoryusage', DWORD),
            ('sv599_enablesoftcompat', BOOL),
            ('sv599_enableforcedlogoff', BOOL),
            ('sv599_timesource', BOOL),
            ('sv599_acceptdownlevelapis', BOOL),
            ('sv599_lmannounce', BOOL),
            ('sv599_domain', LMSTR),
            ('sv599_maxcopyreadlen', DWORD),
            ('sv599_maxcopywritelen', DWORD),
            ('sv599_minkeepsearch', DWORD),
            ('sv599_maxkeepsearch', DWORD),
            ('sv599_minkeepcomplsearch', DWORD),
            ('sv599_maxkeepcomplsearch', DWORD),
            ('sv599_threadcountadd', DWORD),
            ('sv599_numblockthreads', DWORD),
            ('sv599_scavtimeout', DWORD),
            ('sv599_minrcvqueue', DWORD),
            ('sv599_minfreeworkitems', DWORD),
            ('sv599_xactmemsize', DWORD),
            ('sv599_threadpriority', DWORD),
            ('sv599_maxmpxct', DWORD),
            ('sv599_oplockbreakwait', DWORD),
            ('sv599_oplockbreakresponsewait', DWORD),
            ('sv599_enableoplocks', BOOL),
            ('sv599_enableoplockforceclose', BOOL),
            ('sv599_enablefcbopens', BOOL),
            ('sv599_enableraw', BOOL),
            ('sv599_enablesharednetdrives', BOOL),
            ('sv599_minfreeconnections', DWORD),
            ('sv599_maxfreeconnections', DWORD),
            ('sv599_initsesstable', DWORD),
            ('sv599_initconntable', DWORD),
            ('sv599_initfiletable', DWORD),
            ('sv599_initsearchtable', DWORD),
            ('sv599_alertschedule', DWORD),
            ('sv599_errorthreshold', DWORD),
            ('sv599_networkerrorthreshold', DWORD),
            ('sv599_diskspacethreshold', DWORD),
            ('sv599_reserved', DWORD),
            ('sv599_maxlinkdelay', DWORD),
            ('sv599_minlinkthroughput', DWORD),
            ('sv599_linkinfovalidtime', DWORD),
            ('sv599_scavqosinfoupdatetime', DWORD),
            ('sv599_maxworkitemidletime', DWORD),
        ]

        _SERVER_INFO_598._fields_ = [
            ('sv598_maxrawworkitems', DWORD),
            ('sv598_maxthreadsperqueue', DWORD),
            ('sv598_producttype', DWORD),
            ('sv598_serversize', DWORD),
            ('sv598_connectionlessautodisc', DWORD),
            ('sv598_sharingviolationretries', DWORD),
            ('sv598_sharingviolationdelay', DWORD),
            ('sv598_maxglobalopensearch', DWORD),
            ('sv598_removeduplicatesearches', DWORD),
            ('sv598_lockviolationoffset', DWORD),
            ('sv598_lockviolationdelay', DWORD),
            ('sv598_mdlreadswitchover', DWORD),
            ('sv598_cachedopenlimit', DWORD),
            ('sv598_otherqueueaffinity', DWORD),
            ('sv598_restrictnullsessaccess', BOOL),
            ('sv598_enablewfw311directipx', BOOL),
            ('sv598_queuesamplesecs', DWORD),
            ('sv598_balancecount', DWORD),
            ('sv598_preferredaffinity', DWORD),
            ('sv598_maxfreerfcbs', DWORD),
            ('sv598_maxfreemfcbs', DWORD),
            ('sv598_maxfreelfcbs', DWORD),
            ('sv598_maxfreepagedpoolchunks', DWORD),
            ('sv598_minpagedpoolchunksize', DWORD),
            ('sv598_maxpagedpoolchunksize', DWORD),
            ('sv598_sendsfrompreferredprocessor', BOOL),
            ('sv598_cacheddirectorylimit', DWORD),
            ('sv598_maxcopylength', DWORD),
            ('sv598_enablecompression', BOOL),
            ('sv598_autosharewks', BOOL),
            ('sv598_autoshareserver', BOOL),
            ('sv598_enablesecuritysignature', BOOL),
            ('sv598_requiresecuritysignature', BOOL),
            ('sv598_minclientbuffersize', DWORD),
            ('sv598_serverguid', GUID),
            ('sv598_ConnectionNoSessionsTimeout', DWORD),
            ('sv598_IdleThreadTimeOut', DWORD),
            ('sv598_enableW9xsecuritysignature', BOOL),
            ('sv598_enforcekerberosreauthentication', BOOL),
            ('sv598_disabledos', BOOL),
            ('sv598_lowdiskspaceminimum', DWORD),
            ('sv598_disablestrictnamechecking', BOOL),
            ('sv598_enableauthenticateusersharing', BOOL),
        ]

        _SERVER_INFO_1005._fields_ = [
            ('sv1005_comment', LMSTR),
        ]

        _SERVER_INFO_1107._fields_ = [
            ('sv1107_users', DWORD),
        ]

        _SERVER_INFO_1010._fields_ = [
            ('sv1010_disc', LONG),
        ]

        _SERVER_INFO_1016._fields_ = [
            ('sv1016_hidden', BOOL),
        ]

        _SERVER_INFO_1017._fields_ = [
            ('sv1017_announce', DWORD),
        ]

        _SERVER_INFO_1018._fields_ = [
            ('sv1018_anndelta', DWORD),
        ]

        _SERVER_INFO_1501._fields_ = [
            ('sv1501_sessopens', DWORD),
        ]

        _SERVER_INFO_1502._fields_ = [
            ('sv1502_sessvcs', DWORD),
        ]

        _SERVER_INFO_1503._fields_ = [
            ('sv1503_opensearch', DWORD),
        ]

        _SERVER_INFO_1506._fields_ = [
            ('sv1506_maxworkitems', DWORD),
        ]

        _SERVER_INFO_1509._fields_ = [
            ('sv1509_maxrawbuflen', DWORD),
        ]

        _SERVER_INFO_1510._fields_ = [
            ('sv1510_sessusers', DWORD),
        ]

        _SERVER_INFO_1511._fields_ = [
            ('sv1511_sessconns', DWORD),
        ]

        _SERVER_INFO_1512._fields_ = [
            ('sv1512_maxnonpagedmemoryusage', DWORD),
        ]

        _SERVER_INFO_1513._fields_ = [
            ('sv1513_maxpagedmemoryusage', DWORD),
        ]

        _SERVER_INFO_1514._fields_ = [
            ('sv1514_enablesoftcompat', BOOL),
        ]

        _SERVER_INFO_1515._fields_ = [
            ('sv1515_enableforcedlogoff', BOOL),
        ]

        _SERVER_INFO_1516._fields_ = [
            ('sv1516_timesource', BOOL),
        ]

        _SERVER_INFO_1518._fields_ = [
            ('sv1518_lmannounce', BOOL),
        ]

        _SERVER_INFO_1520._fields_ = [
            ('sv1520_maxcopyreadlen', DWORD),
        ]

        _SERVER_INFO_1521._fields_ = [
            ('sv1521_maxcopywritelen', DWORD),
        ]

        _SERVER_INFO_1522._fields_ = [
            ('sv1522_minkeepsearch', DWORD),
        ]

        _SERVER_INFO_1523._fields_ = [
            ('sv1523_maxkeepsearch', DWORD),
        ]

        _SERVER_INFO_1524._fields_ = [
            ('sv1524_minkeepcomplsearch', DWORD),
        ]

        _SERVER_INFO_1525._fields_ = [
            ('sv1525_maxkeepcomplsearch', DWORD),
        ]

        _SERVER_INFO_1528._fields_ = [
            ('sv1528_scavtimeout', DWORD),
        ]

        _SERVER_INFO_1529._fields_ = [
            ('sv1529_minrcvqueue', DWORD),
        ]

        _SERVER_INFO_1530._fields_ = [
            ('sv1530_minfreeworkitems', DWORD),
        ]

        _SERVER_INFO_1533._fields_ = [
            ('sv1533_maxmpxct', DWORD),
        ]

        _SERVER_INFO_1534._fields_ = [
            ('sv1534_oplockbreakwait', DWORD),
        ]

        _SERVER_INFO_1535._fields_ = [
            ('sv1535_oplockbreakresponsewait', DWORD),
        ]

        _SERVER_INFO_1536._fields_ = [
            ('sv1536_enableoplocks', BOOL),
        ]

        _SERVER_INFO_1537._fields_ = [
            ('sv1537_enableoplockforceclose', BOOL),
        ]

        _SERVER_INFO_1538._fields_ = [
            ('sv1538_enablefcbopens', BOOL),
        ]

        _SERVER_INFO_1539._fields_ = [
            ('sv1539_enableraw', BOOL),
        ]

        _SERVER_INFO_1540._fields_ = [
            ('sv1540_enablesharednetdrives', BOOL),
        ]

        _SERVER_INFO_1541._fields_ = [
            ('sv1541_minfreeconnections', BOOL),
        ]

        _SERVER_INFO_1542._fields_ = [
            ('sv1542_maxfreeconnections', BOOL),
        ]

        _SERVER_INFO_1543._fields_ = [
            ('sv1543_initsesstable', DWORD),
        ]

        _SERVER_INFO_1544._fields_ = [
            ('sv1544_initconntable', DWORD),
        ]

        _SERVER_INFO_1545._fields_ = [
            ('sv1545_initfiletable', DWORD),
        ]

        _SERVER_INFO_1546._fields_ = [
            ('sv1546_initsearchtable', DWORD),
        ]

        _SERVER_INFO_1547._fields_ = [
            ('sv1547_alertschedule', DWORD),
        ]

        _SERVER_INFO_1548._fields_ = [
            ('sv1548_errorthreshold', DWORD),
        ]

        _SERVER_INFO_1549._fields_ = [
            ('sv1549_networkerrorthreshold', DWORD),
        ]

        _SERVER_INFO_1550._fields_ = [
            ('sv1550_diskspacethreshold', DWORD),
        ]

        _SERVER_INFO_1552._fields_ = [
            ('sv1552_maxlinkdelay', DWORD),
        ]

        _SERVER_INFO_1553._fields_ = [
            ('sv1553_minlinkthroughput', DWORD),
        ]

        _SERVER_INFO_1554._fields_ = [
            ('sv1554_linkinfovalidtime', DWORD),
        ]

        _SERVER_INFO_1555._fields_ = [
            ('sv1555_scavqosinfoupdatetime', DWORD),
        ]

        _SERVER_INFO_1556._fields_ = [
            ('sv1556_maxworkitemidletime', DWORD),
        ]

        _SERVER_INFO_1557._fields_ = [
            ('sv1557_maxrawworkitems', DWORD),
        ]

        _SERVER_INFO_1560._fields_ = [
            ('sv1560_producttype', DWORD),
        ]

        _SERVER_INFO_1561._fields_ = [
            ('sv1561_serversize', DWORD),
        ]

        _SERVER_INFO_1562._fields_ = [
            ('sv1562_connectionlessautodisc', DWORD),
        ]

        _SERVER_INFO_1563._fields_ = [
            ('sv1563_sharingviolationretries', DWORD),
        ]

        _SERVER_INFO_1564._fields_ = [
            ('sv1564_sharingviolationdelay', DWORD),
        ]

        _SERVER_INFO_1565._fields_ = [
            ('sv1565_maxglobalopensearch', DWORD),
        ]

        _SERVER_INFO_1566._fields_ = [
            ('sv1566_removeduplicatesearches', BOOL),
        ]

        _SERVER_INFO_1567._fields_ = [
            ('sv1567_lockviolationretries', DWORD),
        ]

        _SERVER_INFO_1568._fields_ = [
            ('sv1568_lockviolationoffset', DWORD),
        ]

        _SERVER_INFO_1569._fields_ = [
            ('sv1569_lockviolationdelay', DWORD),
        ]

        _SERVER_INFO_1570._fields_ = [
            ('sv1570_mdlreadswitchover', DWORD),
        ]

        _SERVER_INFO_1571._fields_ = [
            ('sv1571_cachedopenlimit', DWORD),
        ]

        _SERVER_INFO_1572._fields_ = [
            ('sv1572_criticalthreads', DWORD),
        ]

        _SERVER_INFO_1573._fields_ = [
            ('sv1573_restrictnullsessaccess', DWORD),
        ]

        _SERVER_INFO_1574._fields_ = [
            ('sv1574_enablewfw311directipx', DWORD),
        ]

        _SERVER_INFO_1575._fields_ = [
            ('sv1575_otherqueueaffinity', DWORD),
        ]

        _SERVER_INFO_1576._fields_ = [
            ('sv1576_queuesamplesecs', DWORD),
        ]

        _SERVER_INFO_1577._fields_ = [
            ('sv1577_balancecount', DWORD),
        ]

        _SERVER_INFO_1578._fields_ = [
            ('sv1578_preferredaffinity', DWORD),
        ]

        _SERVER_INFO_1579._fields_ = [
            ('sv1579_maxfreerfcbs', DWORD),
        ]

        _SERVER_INFO_1580._fields_ = [
            ('sv1580_maxfreemfcbs', DWORD),
        ]

        _SERVER_INFO_1581._fields_ = [
            ('sv1581_maxfreemlcbs', DWORD),
        ]

        _SERVER_INFO_1582._fields_ = [
            ('sv1582_maxfreepagedpoolchunks', DWORD),
        ]

        _SERVER_INFO_1583._fields_ = [
            ('sv1583_minpagedpoolchunksize', DWORD),
        ]

        _SERVER_INFO_1584._fields_ = [
            ('sv1584_maxpagedpoolchunksize', DWORD),
        ]

        _SERVER_INFO_1585._fields_ = [
            ('sv1585_sendsfrompreferredprocessor', BOOL),
        ]

        _SERVER_INFO_1586._fields_ = [
            ('sv1586_maxthreadsperqueue', DWORD),
        ]

        _SERVER_INFO_1587._fields_ = [
            ('sv1587_cacheddirectorylimit', DWORD),
        ]

        _SERVER_INFO_1588._fields_ = [
            ('sv1588_maxcopylength', DWORD),
        ]

        _SERVER_INFO_1590._fields_ = [
            ('sv1590_enablecompression', DWORD),
        ]

        _SERVER_INFO_1591._fields_ = [
            ('sv1591_autosharewks', DWORD),
        ]

        _SERVER_INFO_1592._fields_ = [
            ('sv1592_autosharewks', DWORD),
        ]

        _SERVER_INFO_1593._fields_ = [
            ('sv1593_enablesecuritysignature', DWORD),
        ]

        _SERVER_INFO_1594._fields_ = [
            ('sv1594_requiresecuritysignature', DWORD),
        ]

        _SERVER_INFO_1595._fields_ = [
            ('sv1595_minclientbuffersize', DWORD),
        ]

        _SERVER_INFO_1596._fields_ = [
            ('sv1596_ConnectionNoSessionsTimeout', DWORD),
        ]

        _SERVER_INFO_1597._fields_ = [
            ('sv1597_IdleThreadTimeOut', DWORD),
        ]

        _SERVER_INFO_1598._fields_ = [
            ('sv1598_enableW9xsecuritysignature', DWORD),
        ]

        _SERVER_INFO_1599._fields_ = [
            ('sv1598_enforcekerberosreauthentication', BOOLEAN),
        ]

        _SERVER_INFO_1600._fields_ = [
            ('sv1598_disabledos', BOOLEAN),
        ]

        _SERVER_INFO_1601._fields_ = [
            ('sv1598_lowdiskspaceminimum', DWORD),
        ]

        _SERVER_INFO_1602._fields_ = [
            ('sv_1598_disablestrictnamechecking', BOOL),
        ]

        # A special structure definition is required in order for this
        # structure to work with RPC. The problem is that having
        # addresslength
        # indicate the number of bytes in address means that RPC must know
        # the
        # link between the two.
        if defined(MIDL_PASS):
            _SERVER_TRANSPORT_INFO_0._fields_ = [
                ('svti0_numberofvcs', DWORD),
                ('svti0_transportname', LMSTR),
                ('svti0_transportaddress', LPBYTE),
                ('svti0_transportaddresslength', DWORD),
                ('svti0_networkaddress', LMSTR),
            ]

            _SERVER_TRANSPORT_INFO_1._fields_ = [
                ('svti1_numberofvcs', DWORD),
                ('svti1_transportname', LMSTR),
                ('svti1_transportaddress', LPBYTE),
                ('svti1_transportaddresslength', DWORD),
                ('svti1_networkaddress', LMSTR),
                ('svti1_domain', LMSTR),
            ]

            _SERVER_TRANSPORT_INFO_2._fields_ = [
                ('svti2_numberofvcs', DWORD),
                ('svti2_transportname', LMSTR),
                ('svti2_transportaddress', LPBYTE),
                ('svti2_transportaddresslength', DWORD),
                ('svti2_networkaddress', LMSTR),
                ('svti2_domain', LMSTR),
                ('svti2_flags', ULONG),
            ]

            _SERVER_TRANSPORT_INFO_3._fields_ = [
                ('svti3_numberofvcs', DWORD),
                ('svti3_transportname', LMSTR),
                ('svti3_transportaddress', LPBYTE),
                ('svti3_transportaddresslength', DWORD),
                ('svti3_networkaddress', LMSTR),
                ('svti3_domain', LMSTR),
                ('svti3_flags', ULONG),
                ('svti3_passwordlength', DWORD),
                ('svti3_password', BYTE * 256),
            ]
        else:
            _SERVER_TRANSPORT_INFO_0._fields_ = [
                ('svti0_numberofvcs', DWORD),
                ('svti0_transportname', LMSTR),
                ('svti0_transportaddress', LPBYTE),
                ('svti0_transportaddresslength', DWORD),
                ('svti0_networkaddress', LMSTR),
            ]

            _SERVER_TRANSPORT_INFO_1._fields_ = [
                ('svti1_numberofvcs', DWORD),
                ('svti1_transportname', LMSTR),
                ('svti1_transportaddress', LPBYTE),
                ('svti1_transportaddresslength', DWORD),
                ('svti1_networkaddress', LMSTR),
                ('svti1_domain', LMSTR),
            ]

            _SERVER_TRANSPORT_INFO_2._fields_ = [
                ('svti2_numberofvcs', DWORD),
                ('svti2_transportname', LMSTR),
                ('svti2_transportaddress', LPBYTE),
                ('svti2_transportaddresslength', DWORD),
                ('svti2_networkaddress', LMSTR),
                ('svti2_domain', LMSTR),
                ('svti2_flags', ULONG),
            ]

            _SERVER_TRANSPORT_INFO_3._fields_ = [
                ('svti3_numberofvcs', DWORD),
                ('svti3_transportname', LMSTR),
                ('svti3_transportaddress', LPBYTE),
                ('svti3_transportaddresslength', DWORD),
                ('svti3_networkaddress', LMSTR),
                ('svti3_domain', LMSTR),
                ('svti3_flags', ULONG),
                ('svti3_passwordlength', DWORD),
                ('svti3_password', BYTE * 256),
            ]
        # END IF

        # Defines - SERVER
        # The platform ID indicates the levels to use for platform-specific
        # information.
        SV_PLATFORM_ID_OS2 = 400
        SV_PLATFORM_ID_NT = 500

        # Mask to be applied to svX_version_major in order to obtain
        # the major version number.
        MAJOR_VERSION_MASK = 0x0F

        # Bit-mapped values for svX_type fields. X = 1, 2 or 3.
        SV_TYPE_WORKSTATION = 0x00000001
        SV_TYPE_SERVER = 0x00000002
        SV_TYPE_SQLSERVER = 0x00000004
        SV_TYPE_DOMAIN_CTRL = 0x00000008
        SV_TYPE_DOMAIN_BAKCTRL = 0x00000010
        SV_TYPE_TIME_SOURCE = 0x00000020
        SV_TYPE_AFP = 0x00000040
        SV_TYPE_NOVELL = 0x00000080
        SV_TYPE_DOMAIN_MEMBER = 0x00000100
        SV_TYPE_PRINTQ_SERVER = 0x00000200
        SV_TYPE_DIALIN_SERVER = 0x00000400
        SV_TYPE_XENIX_SERVER = 0x00000800
        SV_TYPE_SERVER_UNIX = SV_TYPE_XENIX_SERVER
        SV_TYPE_NT = 0x00001000
        SV_TYPE_WFW = 0x00002000
        SV_TYPE_SERVER_MFPN = 0x00004000
        SV_TYPE_SERVER_NT = 0x00008000
        SV_TYPE_POTENTIAL_BROWSER = 0x00010000
        SV_TYPE_BACKUP_BROWSER = 0x00020000
        SV_TYPE_MASTER_BROWSER = 0x00040000
        SV_TYPE_DOMAIN_MASTER = 0x00080000
        SV_TYPE_SERVER_OSF = 0x00100000
        SV_TYPE_SERVER_VMS = 0x00200000
        SV_TYPE_WINDOWS = 0x00400000  # Windows95 and above
        SV_TYPE_DFS = 0x00800000  # Root of a DFS tree
        SV_TYPE_CLUSTER_NT = 0x01000000  # NT Cluster
        SV_TYPE_TERMINALSERVER = 0x02000000  # Terminal Server(Hydra)
        SV_TYPE_CLUSTER_VS_NT = 0x04000000  # NT Cluster Virtual Server Name
        SV_TYPE_DCE = 0x10000000  # IBM DSS (Directory and Security Services) or equivalent
        SV_TYPE_ALTERNATE_XPORT = 0x20000000  # return list for alternate transport
        SV_TYPE_LOCAL_LIST_ONLY = 0x40000000  # Return local list only
        SV_TYPE_DOMAIN_ENUM = 0x80000000
        SV_TYPE_ALL = 0xFFFFFFFF  # handy for NetServerEnum2

        # Special value for sv102_disc that specifies infinite disconnect
        # time.
        SV_NODISC = -1L  # No autodisconnect timeout enforced

        # Values of svX_security field. X = 2 or 3.
        SV_USERSECURITY = 1
        SV_SHARESECURITY = 0

        # Values of svX_hidden field. X = 2 or 3.
        SV_HIDDEN = 1
        SV_VISIBLE = 0

        # Values for ParmError parameter to NetServerSetInfo.
        SV_PLATFORM_ID_PARMNUM = 101
        SV_NAME_PARMNUM = 102
        SV_VERSION_MAJOR_PARMNUM = 103
        SV_VERSION_MINOR_PARMNUM = 104
        SV_TYPE_PARMNUM = 105
        SV_COMMENT_PARMNUM = 5
        SV_USERS_PARMNUM = 107
        SV_DISC_PARMNUM = 10
        SV_HIDDEN_PARMNUM = 16
        SV_ANNOUNCE_PARMNUM = 17
        SV_ANNDELTA_PARMNUM = 18
        SV_USERPATH_PARMNUM = 112
        SV_ULIST_MTIME_PARMNUM = 401
        SV_GLIST_MTIME_PARMNUM = 402
        SV_ALIST_MTIME_PARMNUM = 403
        SV_ALERTS_PARMNUM = 11
        SV_SECURITY_PARMNUM = 405
        SV_NUMADMIN_PARMNUM = 406
        SV_LANMASK_PARMNUM = 407
        SV_GUESTACC_PARMNUM = 408
        SV_CHDEVQ_PARMNUM = 410
        SV_CHDEVJOBS_PARMNUM = 411
        SV_CONNECTIONS_PARMNUM = 412
        SV_SHARES_PARMNUM = 413
        SV_OPENFILES_PARMNUM = 414
        SV_SESSREQS_PARMNUM = 417
        SV_ACTIVELOCKS_PARMNUM = 419
        SV_NUMREQBUF_PARMNUM = 420
        SV_NUMBIGBUF_PARMNUM = 422
        SV_NUMFILETASKS_PARMNUM = 423
        SV_ALERTSCHED_PARMNUM = 37
        SV_ERRORALERT_PARMNUM = 38
        SV_LOGONALERT_PARMNUM = 39
        SV_ACCESSALERT_PARMNUM = 40
        SV_DISKALERT_PARMNUM = 41
        SV_NETIOALERT_PARMNUM = 42
        SV_MAXAUDITSZ_PARMNUM = 43
        SV_SRVHEURISTICS_PARMNUM = 431
        SV_SESSOPENS_PARMNUM = 501
        SV_SESSVCS_PARMNUM = 502
        SV_OPENSEARCH_PARMNUM = 503
        SV_SIZREQBUF_PARMNUM = 504
        SV_INITWORKITEMS_PARMNUM = 505
        SV_MAXWORKITEMS_PARMNUM = 506
        SV_RAWWORKITEMS_PARMNUM = 507
        SV_IRPSTACKSIZE_PARMNUM = 508
        SV_MAXRAWBUFLEN_PARMNUM = 509
        SV_SESSUSERS_PARMNUM = 510
        SV_SESSCONNS_PARMNUM = 511
        SV_MAXNONPAGEDMEMORYUSAGE_PARMNUM = 512
        SV_MAXPAGEDMEMORYUSAGE_PARMNUM = 513
        SV_ENABLESOFTCOMPAT_PARMNUM = 514
        SV_ENABLEFORCEDLOGOFF_PARMNUM = 515
        SV_TIMESOURCE_PARMNUM = 516
        SV_ACCEPTDOWNLEVELAPIS_PARMNUM = 517
        SV_LMANNOUNCE_PARMNUM = 518
        SV_DOMAIN_PARMNUM = 519
        SV_MAXCOPYREADLEN_PARMNUM = 520
        SV_MAXCOPYWRITELEN_PARMNUM = 521
        SV_MINKEEPSEARCH_PARMNUM = 522
        SV_MAXKEEPSEARCH_PARMNUM = 523
        SV_MINKEEPCOMPLSEARCH_PARMNUM = 524
        SV_MAXKEEPCOMPLSEARCH_PARMNUM = 525
        SV_THREADCOUNTADD_PARMNUM = 526
        SV_NUMBLOCKTHREADS_PARMNUM = 527
        SV_SCAVTIMEOUT_PARMNUM = 528
        SV_MINRCVQUEUE_PARMNUM = 529
        SV_MINFREEWORKITEMS_PARMNUM = 530
        SV_XACTMEMSIZE_PARMNUM = 531
        SV_THREADPRIORITY_PARMNUM = 532
        SV_MAXMPXCT_PARMNUM = 533
        SV_OPLOCKBREAKWAIT_PARMNUM = 534
        SV_OPLOCKBREAKRESPONSEWAIT_PARMNUM = 535
        SV_ENABLEOPLOCKS_PARMNUM = 536
        SV_ENABLEOPLOCKFORCECLOSE_PARMNUM = 537
        SV_ENABLEFCBOPENS_PARMNUM = 538
        SV_ENABLERAW_PARMNUM = 539
        SV_ENABLESHAREDNETDRIVES_PARMNUM = 540
        SV_MINFREECONNECTIONS_PARMNUM = 541
        SV_MAXFREECONNECTIONS_PARMNUM = 542
        SV_INITSESSTABLE_PARMNUM = 543
        SV_INITCONNTABLE_PARMNUM = 544
        SV_INITFILETABLE_PARMNUM = 545
        SV_INITSEARCHTABLE_PARMNUM = 546
        SV_ALERTSCHEDULE_PARMNUM = 547
        SV_ERRORTHRESHOLD_PARMNUM = 548
        SV_NETWORKERRORTHRESHOLD_PARMNUM = 549
        SV_DISKSPACETHRESHOLD_PARMNUM = 550
        SV_MAXLINKDELAY_PARMNUM = 552
        SV_MINLINKTHROUGHPUT_PARMNUM = 553
        SV_LINKINFOVALIDTIME_PARMNUM = 554
        SV_SCAVQOSINFOUPDATETIME_PARMNUM = 555
        SV_MAXWORKITEMIDLETIME_PARMNUM = 556
        SV_MAXRAWWORKITEMS_PARMNUM = 557
        SV_PRODUCTTYPE_PARMNUM = 560
        SV_SERVERSIZE_PARMNUM = 561
        SV_CONNECTIONLESSAUTODISC_PARMNUM = 562
        SV_SHARINGVIOLATIONRETRIES_PARMNUM = 563
        SV_SHARINGVIOLATIONDELAY_PARMNUM = 564
        SV_MAXGLOBALOPENSEARCH_PARMNUM = 565
        SV_REMOVEDUPLICATESEARCHES_PARMNUM = 566
        SV_LOCKVIOLATIONRETRIES_PARMNUM = 567
        SV_LOCKVIOLATIONOFFSET_PARMNUM = 568
        SV_LOCKVIOLATIONDELAY_PARMNUM = 569
        SV_MDLREADSWITCHOVER_PARMNUM = 570
        SV_CACHEDOPENLIMIT_PARMNUM = 571
        SV_CRITICALTHREADS_PARMNUM = 572
        SV_RESTRICTNULLSESSACCESS_PARMNUM = 573
        SV_ENABLEWFW311DIRECTIPX_PARMNUM = 574
        SV_OTHERQUEUEAFFINITY_PARMNUM = 575
        SV_QUEUESAMPLESECS_PARMNUM = 576
        SV_BALANCECOUNT_PARMNUM = 577
        SV_PREFERREDAFFINITY_PARMNUM = 578
        SV_MAXFREERFCBS_PARMNUM = 579
        SV_MAXFREEMFCBS_PARMNUM = 580
        SV_MAXFREELFCBS_PARMNUM = 581
        SV_MAXFREEPAGEDPOOLCHUNKS_PARMNUM = 582
        SV_MINPAGEDPOOLCHUNKSIZE_PARMNUM = 583
        SV_MAXPAGEDPOOLCHUNKSIZE_PARMNUM = 584
        SV_SENDSFROMPREFERREDPROCESSOR_PARMNUM = 585
        SV_MAXTHREADSPERQUEUE_PARMNUM = 586
        SV_CACHEDDIRECTORYLIMIT_PARMNUM = 587
        SV_MAXCOPYLENGTH_PARMNUM = 588
        SV_ENABLECOMPRESSION_PARMNUM = 590
        SV_AUTOSHAREWKS_PARMNUM = 591
        SV_AUTOSHARESERVER_PARMNUM = 592
        SV_ENABLESECURITYSIGNATURE_PARMNUM = 593
        SV_REQUIRESECURITYSIGNATURE_PARMNUM = 594
        SV_MINCLIENTBUFFERSIZE_PARMNUM = 595
        SV_CONNECTIONNOSESSIONSTIMEOUT_PARMNUM = 596
        SV_IDLETHREADTIMEOUT_PARMNUM = 597
        SV_ENABLEW9XSECURITYSIGNATURE_PARMNUM = 598
        SV_ENFORCEKERBEROSREAUTHENTICATION_PARMNUM = 599
        SV_DISABLEDOS_PARMNUM = 600
        SV_LOWDISKSPACEMINIMUM_PARMNUM = 601
        SV_DISABLESTRICTNAMECHECKING_PARMNUM = 602
        SV_ENABLEAUTHENTICATEUSERSHARING_PARMNUM = 603

        # Single-field infolevels for NetServerSetInfo.
        SV_COMMENT_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + SV_COMMENT_PARMNUM
        SV_USERS_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + SV_USERS_PARMNUM
        SV_DISC_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + SV_DISC_PARMNUM
        SV_HIDDEN_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + SV_HIDDEN_PARMNUM
        SV_ANNOUNCE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ANNOUNCE_PARMNUM
        )
        SV_ANNDELTA_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ANNDELTA_PARMNUM
        )
        SV_SESSOPENS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_SESSOPENS_PARMNUM
        )
        SV_SESSVCS_INFOLEVEL = PARMNUM_BASE_INFOLEVEL + SV_SESSVCS_PARMNUM
        SV_OPENSEARCH_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_OPENSEARCH_PARMNUM
        )
        SV_MAXWORKITEMS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXWORKITEMS_PARMNUM
        )
        SV_MAXRAWBUFLEN_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXRAWBUFLEN_PARMNUM
        )
        SV_SESSUSERS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_SESSUSERS_PARMNUM
        )
        SV_SESSCONNS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_SESSCONNS_PARMNUM
        )
        SV_MAXNONPAGEDMEMORYUSAGE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXNONPAGEDMEMORYUSAGE_PARMNUM
        )
        SV_MAXPAGEDMEMORYUSAGE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXPAGEDMEMORYUSAGE_PARMNUM
        )
        SV_ENABLESOFTCOMPAT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ENABLESOFTCOMPAT_PARMNUM
        )
        SV_ENABLEFORCEDLOGOFF_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ENABLEFORCEDLOGOFF_PARMNUM
        )
        SV_TIMESOURCE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_TIMESOURCE_PARMNUM
        )
        SV_LMANNOUNCE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_LMANNOUNCE_PARMNUM
        )
        SV_MAXCOPYREADLEN_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXCOPYREADLEN_PARMNUM
        )
        SV_MAXCOPYWRITELEN_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXCOPYWRITELEN_PARMNUM
        )
        SV_MINKEEPSEARCH_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MINKEEPSEARCH_PARMNUM
        )
        SV_MAXKEEPSEARCH_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXKEEPSEARCH_PARMNUM
        )
        SV_MINKEEPCOMPLSEARCH_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MINKEEPCOMPLSEARCH_PARMNUM
        )
        SV_MAXKEEPCOMPLSEARCH_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXKEEPCOMPLSEARCH_PARMNUM
        )
        SV_SCAVTIMEOUT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_SCAVTIMEOUT_PARMNUM
        )
        SV_MINRCVQUEUE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MINRCVQUEUE_PARMNUM
        )
        SV_MINFREEWORKITEMS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MINFREEWORKITEMS_PARMNUM
        )
        SV_MAXMPXCT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXMPXCT_PARMNUM
        )
        SV_OPLOCKBREAKWAIT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_OPLOCKBREAKWAIT_PARMNUM
        )
        SV_OPLOCKBREAKRESPONSEWAIT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_OPLOCKBREAKRESPONSEWAIT_PARMNUM
        )
        SV_ENABLEOPLOCKS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ENABLEOPLOCKS_PARMNUM
        )
        SV_ENABLEOPLOCKFORCECLOSE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ENABLEOPLOCKFORCECLOSE_PARMNUM
        )
        SV_ENABLEFCBOPENS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ENABLEFCBOPENS_PARMNUM
        )
        SV_ENABLERAW_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ENABLERAW_PARMNUM
        )
        SV_ENABLESHAREDNETDRIVES_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ENABLESHAREDNETDRIVES_PARMNUM
        )
        SV_MINFREECONNECTIONS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MINFREECONNECTIONS_PARMNUM
        )
        SV_MAXFREECONNECTIONS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXFREECONNECTIONS_PARMNUM
        )
        SV_INITSESSTABLE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_INITSESSTABLE_PARMNUM
        )
        SV_INITCONNTABLE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_INITCONNTABLE_PARMNUM
        )
        SV_INITFILETABLE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_INITFILETABLE_PARMNUM
        )
        SV_INITSEARCHTABLE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_INITSEARCHTABLE_PARMNUM
        )
        SV_ALERTSCHEDULE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ALERTSCHEDULE_PARMNUM
        )
        SV_ERRORTHRESHOLD_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ERRORTHRESHOLD_PARMNUM
        )
        SV_NETWORKERRORTHRESHOLD_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_NETWORKERRORTHRESHOLD_PARMNUM
        )
        SV_DISKSPACETHRESHOLD_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_DISKSPACETHRESHOLD_PARMNUM
        )
        SV_MAXLINKDELAY_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXLINKDELAY_PARMNUM
        )
        SV_MINLINKTHROUGHPUT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MINLINKTHROUGHPUT_PARMNUM
        )
        SV_LINKINFOVALIDTIME_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_LINKINFOVALIDTIME_PARMNUM
        )
        SV_SCAVQOSINFOUPDATETIME_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_SCAVQOSINFOUPDATETIME_PARMNUM
        )
        SV_MAXWORKITEMIDLETIME_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXWORKITEMIDLETIME_PARMNUM
        )
        SV_MAXRAWWORKITEMS_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXRAWWORKITEMS_PARMNUM
        )
        SV_PRODUCTTYPE_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_PRODUCTTYPE_PARMNUM
        )
        SV_SERVERSIZE_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_SERVERSIZE_PARMNUM
        )
        SV_CONNECTIONLESSAUTODISC_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_CONNECTIONLESSAUTODISC_PARMNUM
        )
        SV_SHARINGVIOLATIONRETRIES_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_SHARINGVIOLATIONRETRIES_PARMNUM
        )
        SV_SHARINGVIOLATIONDELAY_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_SHARINGVIOLATIONDELAY_PARMNUM
        )
        SV_MAXGLOBALOPENSEARCH_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXGLOBALOPENSEARCH_PARMNUM
        )
        SV_REMOVEDUPLICATESEARCHES_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_REMOVEDUPLICATESEARCHES_PARMNUM
        )
        SV_LOCKVIOLATIONRETRIES_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_LOCKVIOLATIONRETRIES_PARMNUM
        )
        SV_LOCKVIOLATIONOFFSET_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_LOCKVIOLATIONOFFSET_PARMNUM
        )
        SV_LOCKVIOLATIONDELAY_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_LOCKVIOLATIONDELAY_PARMNUM
        )
        SV_MDLREADSWITCHOVER_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MDLREADSWITCHOVER_PARMNUM
        )
        SV_CACHEDOPENLIMIT_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_CACHEDOPENLIMIT_PARMNUM
        )
        SV_CRITICALTHREADS_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_CRITICALTHREADS_PARMNUM
        )
        SV_RESTRICTNULLSESSACCESS_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_RESTRICTNULLSESSACCESS_PARMNUM
        )
        SV_ENABLEWFW311DIRECTIPX_INFOLOEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ENABLEWFW311DIRECTIPX_PARMNUM
        )
        SV_OTHERQUEUEAFFINITY_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_OTHERQUEUEAFFINITY_PARMNUM
        )
        SV_QUEUESAMPLESECS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_QUEUESAMPLESECS_PARMNUM
        )
        SV_BALANCECOUNT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_BALANCECOUNT_PARMNUM
        )
        SV_PREFERREDAFFINITY_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_PREFERREDAFFINITY_PARMNUM
        )
        SV_MAXFREERFCBS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXFREERFCBS_PARMNUM
        )
        SV_MAXFREEMFCBS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXFREEMFCBS_PARMNUM
        )
        SV_MAXFREELFCBS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXFREELFCBS_PARMNUM
        )
        SV_MAXFREEPAGEDPOOLCHUNKS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXFREEPAGEDPOOLCHUNKS_PARMNUM
        )
        SV_MINPAGEDPOOLCHUNKSIZE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MINPAGEDPOOLCHUNKSIZE_PARMNUM
        )
        SV_MAXPAGEDPOOLCHUNKSIZE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXPAGEDPOOLCHUNKSIZE_PARMNUM
        )
        SV_SENDSFROMPREFERREDPROCESSOR_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_SENDSFROMPREFERREDPROCESSOR_PARMNUM
        )
        SV_MAXTHREADSPERQUEUE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXTHREADSPERQUEUE_PARMNUM
        )
        SV_CACHEDDIRECTORYLIMIT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_CACHEDDIRECTORYLIMIT_PARMNUM
        )
        SV_MAXCOPYLENGTH_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MAXCOPYLENGTH_PARMNUM
        )
        SV_ENABLECOMPRESSION_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ENABLECOMPRESSION_PARMNUM
        )
        SV_AUTOSHAREWKS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_AUTOSHAREWKS_PARMNUM
        )
        SV_AUTOSHARESERVER_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_AUTOSHARESERVER_PARMNUM
        )
        SV_ENABLESECURITYSIGNATURE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ENABLESECURITYSIGNATURE_PARMNUM
        )
        SV_REQUIRESECURITYSIGNATURE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_REQUIRESECURITYSIGNATURE_PARMNUM
        )
        SV_MINCLIENTBUFFERSIZE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_MINCLIENTBUFFERSIZE_PARMNUM
        )
        SV_CONNECTIONNOSESSIONSTIMEOUT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_CONNECTIONNOSESSIONSTIMEOUT_PARMNUM
        )
        SV_IDLETHREADTIMEOUT_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_IDLETHREADTIMEOUT_PARMNUM
        )
        SV_ENABLEW9XSECURITYSIGNATURE_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ENABLEW9XSECURITYSIGNATURE_PARMNUM
        )
        SV_ENFORCEKERBEROSREAUTHENTICATION_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ENFORCEKERBEROSREAUTHENTICATION_PARMNUM
        )
        SV_DISABLEDOS_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_DISABLEDOS_PARMNUM
        )
        SV_LOWDISKSPACEMINIMUM_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_LOWDISKSPACEMINIMUM_PARMNUM
        )
        SV_DISABLESTRICTNAMECHECKING_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_DISABLESTRICTNAMECHECKING_PARMNUM
        )
        SV_ENABLEAUTHENTICATEUSERSHARING_INFOLEVEL = (
            PARMNUM_BASE_INFOLEVEL + SV_ENABLEAUTHENTICATEUSERSHARING_PARMNUM
        )
        SVI1_NUM_ELEMENTS = 5
        SVI2_NUM_ELEMENTS = 40
        SVI3_NUM_ELEMENTS = 44

        # Maxmimum length for command string to NetServerAdminCommand.
        SV_MAX_CMD_LEN = PATHLEN

        # Masks describing AUTOPROFILE parameters
        SW_AUTOPROF_LOAD_MASK = 0x1
        SW_AUTOPROF_SAVE_MASK = 0x2

        # Max size of svX_srvheuristics.
        SV_MAX_SRV_HEUR_LEN = 32  # Max heuristics info string length.

        # Equate for use with sv102_licenses.
        SV_USERS_PER_LICENSE = 5

        # Equate for use with svti2_flags in NetServerTransportAddEx.
        SVTI2_REMAP_PIPE_NAMES = 0x02
        SVTI2_SCOPED_NAME = 0x04

        # new Win8 flags for clustering
        # the values should be changed once new sscore functionality is
        # impelmented
        # SVTI2_CLUSTER_NAME means that scope belongs to clustering
        SVTI2_CLUSTER_NAME = 0x08

        # SVTI2_CLUSTER_DNN_NAME means that scope belongs to scale-out
        # clustering
        SVTI2_CLUSTER_DNN_NAME = 0x10

        # Means that transport address field passed with the server
        # transport info
        # struct contains a unicode string.
        SVTI2_UNICODE_TRANSPORT_ADDRESS = 0x20

        # Reserved for Internal Use
        SVTI2_RESERVED1 = 0x1000
        SVTI2_RESERVED2 = 0x2000
        SVTI2_RESERVED3 = 0x4000
        SVTI2_VALID_FLAGS = (
            SVTI2_REMAP_PIPE_NAMES |
            SVTI2_SCOPED_NAME |
            SVTI2_CLUSTER_NAME |
            SVTI2_CLUSTER_DNN_NAME |
            SVTI2_UNICODE_TRANSPORT_ADDRESS
        )

        # Server capability information
        SRV_SUPPORT_HASH_GENERATION = 0x0001
        SRV_HASH_GENERATION_ACTIVE = 0x0002
        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
 # END IF   _LMSERVER_


