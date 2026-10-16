# Table · Anticipa · source evidence

Read-only Figma evidence. 2026-10-01. Inspection: PARTIAL_DEPENDENCY_METADATA. [Source](https://www.figma.com/design/zuUq3gcF9T3CLid44bjY6W/Anticipa-Junio2026?node-id=15006-84823). [Deterministic model](table-anticipa.source.component-contract.yaml).

## 1. Component Identity

Organism / Anticipa / Table, 15006:84823, key 2554d8d2676ae38aac0d9e92716a32e46876cd46.1280×412. Parent Table17001:89457; page Components17001:89455.

## 2. Anatomy

Table → Header + Rows SLOT

Header → Checkbox (hidden) + Action header (hidden) + Cells SLOT

Row → Checkbox (hidden) + Actions Cell (hidden) + Cells SLOT

Hover Row → Checkbox + Actions Cell + DotsThree action + Cells SLOT

Header Cell → Logo (hidden) + Text + Sort (hidden)

Body Cell → Badge (hidden) + Text + Copy (hidden)

Actions Cell → Actions SLOT

## 3. Dependencies

- Molecule / Anticipa / TableHeader: 1instances; key `56fa094afd2ba9e0fc614602ff2096386c254431`; LOCAL; PARTIALLY_RESOLVED.
- type=unselected, state=enabled: 11instances; key `70b8f0441f67fc2234a47478753cac146164d4d3`; REMOTE; PARTIALLY_RESOLVED.
- Atom / Table / Header / Cell: 8instances; key `b4dc2065de621a9e0e27934497fc0f222ab6a7d2`; LOCAL; PARTIALLY_RESOLVED.
- product=contabilidad, type=isotipo: 18instances; key `36ccde1b4574576c9382e70371f819f71ac240d5`; REMOTE; PARTIALLY_RESOLVED.
- sort-down: 8instances; key `f6a9dc8dc9a0cd278cdf840d16509218eba83d22`; REMOTE; PARTIALLY_RESOLVED.
- hover=false: 10instances; key `efc79c22caa601189fa3f4d8d170f54f8d199b29`; LOCAL; PARTIALLY_RESOLVED.
- Atom / Table / Content / Cell / Actions: 10instances; key `ac5623208273ee4846d77ed3e69df27ecf4a6107`; LOCAL; PARTIALLY_RESOLVED.
- state=default, size=middle, type=outline: 10instances; key `0954da38c91f3b5766de68697db73a309b25cf21`; REMOTE; PARTIALLY_RESOLVED.
- Format=Outline, Weight=Light: 10instances; key `93c1dc4338b4b467d084ec42fd9890a5079bd518`; REMOTE; PARTIALLY_RESOLVED.
- type=number, size=middle: 20instances; key `06df8e9033e095bd1ca776691d73501daf5fdda9`; REMOTE; PARTIALLY_RESOLVED.
- Atom / Table / Content / Cell: 70instances; key `707a874a7e13733ca02c6503f2dc910fe31c54a5`; LOCAL; PARTIALLY_RESOLVED.
- type=success: 70instances; key `59430ef2a0f48aeb6f70e4740ff97b6bc8391ce4`; REMOTE; PARTIALLY_RESOLVED.
- Format=Outline, Weight=Fill: 70instances; key `2a6fa63a7acf982fd583c591681a3d9fe1f1abe1`; REMOTE; PARTIALLY_RESOLVED.
- Format=Outline, Weight=Fill: 70instances; key `3f0d7ae9a02577d4fb4e615737d09fa1b49ec230`; REMOTE; PARTIALLY_RESOLVED.
- copy: 70instances; key `7b0069586b87eae9c4fd07924da8d6d06cdad66e`; REMOTE; PARTIALLY_RESOLVED.

## 4. Properties

Native Slots Rows/Cells/Actions. Optional selection, actions, brand, sort, status and copy are hidden by default. Text has no public TEXT property in the cell mains.

## 5. Variants

Row: hover=false/true. Table itself is a standalone component.

## 6. States

Observed Default composition; Hover main inspected. Loading/error/empty semantics require definition.

## 7. Layout

{"baseline":[1280,412],"headerHeight":52,"rowHeight":36,"columns":[156,371.999755859375,132,224,156,88,88],"rowPaddingLR":8,"cellGap":8,"hoverWidth":1287.999755859375,"hoverFirstCell":132}

Exact cells/containers in snapshots; no assumed responsive breakpoint.

## 8. Visual Styles

{"header":"#EFF3FF","row":"#FFFFFF","hover":"#F1F5F9","border":"#E2E8F0","headerText":"#0F172A","bodyText":"#000000","radius":8}

## 9. Typography

Manrope Bold/Regular 14/20, tracking0, single line with ending truncation

## 10. Tokens

- `Size/ Radius / Base` (VariableID:15006:84096), FLOAT, LOCAL; sample `15006:84823.boundVariables.topLeftRadius`; 4references. Aliases in YAML/snapshot.
- `Color/background/informative` (VariableID:17569:27784), COLOR, LOCAL; sample `15006:83464.boundVariables.fills.0`; 2references. Aliases in YAML/snapshot.
- `Color/stroke/base` (VariableID:17569:27786), COLOR, LOCAL; sample `15006:83464.boundVariables.strokes.0`; 154references. Aliases in YAML/snapshot.
- `color/text/primary` (VariableID:ca2ca2cc17d99357b05a0401d6eb230dfad804b5/3639:893), COLOR, REMOTE; sample `I15006:83464;15006:86218;1221:28821.boundVariables.fills.0`; 44references. Aliases in YAML/snapshot.
- `font/family/base` (VariableID:5b6478e0ce1305efedeaf4a605843e3af57a32ca/8394:2), STRING, REMOTE; sample `I15006:83464;15006:86218;1221:28821.boundVariables.fontFamily.0`; 32references. Aliases in YAML/snapshot.
- `font/size/sm` (VariableID:127a590c83af7e9167ebd4daaca4658d7e6ca288/3639:862), FLOAT, REMOTE; sample `I15006:83464;15006:86218;1221:28821.boundVariables.fontSize.0`; 22references. Aliases in YAML/snapshot.
- `radius/md` (VariableID:60ddc1af6f284d6ebc5ef222764a2ff061a7cf3f/45:522), FLOAT, REMOTE; sample `I15006:83464;15006:86218;1221:28824.boundVariables.topLeftRadius`; 44references. Aliases in YAML/snapshot.
- `stroke/stroke-focus` (VariableID:06a98ee346a24b7252c46757d35453bf61945838/4331:1213), FLOAT, REMOTE; sample `I15006:83464;15006:86218;1221:28824.boundVariables.strokeTopWeight`; 44references. Aliases in YAML/snapshot.
- `color/border/default` (VariableID:6895a1ae8da99e8cd2d5a008d5d4bc9710695b39/3639:905), COLOR, REMOTE; sample `I15006:83464;15006:86218;1221:28824.boundVariables.strokes.0`; 22references. Aliases in YAML/snapshot.
- `Color/text/base` (VariableID:17569:27770), COLOR, LOCAL; sample `I15006:83464;15006:86229;15001:198354.boundVariables.fills.0`; 16references. Aliases in YAML/snapshot.
- `Font/Primary` (VariableID:15006:75178), STRING, LOCAL; sample `I15006:83464;15006:86229;15001:198354.boundVariables.fontFamily.0`; 78references. Aliases in YAML/snapshot.
- `Size/Font/Body/Base` (VariableID:15006:75542), FLOAT, LOCAL; sample `I15006:83464;15006:86229;15001:198354.boundVariables.fontSize.0`; 78references. Aliases in YAML/snapshot.
- `Color / Text / Base` (VariableID:15005:75097), COLOR, LOCAL; sample `I15006:83464;15006:86229;15001:198355;1287:5444.boundVariables.fills.0`; 296references. Aliases in YAML/snapshot.
- `Color/background/base` (VariableID:17569:27778), COLOR, LOCAL; sample `15006:84201.boundVariables.fills.0`; 20references. Aliases in YAML/snapshot.
- `spacing/sm` (VariableID:634220d13f50e842b56b814d7b2f7d8049cc0c95/3639:806), FLOAT, REMOTE; sample `I15006:84201;17279:10633;17274:6107.boundVariables.paddingLeft`; 220references. Aliases in YAML/snapshot.
- `radius/md` (VariableID:31c39dae3354372bf695953f2b7d26172742bdeb/3639:799), FLOAT, REMOTE; sample `I15006:84201;17279:10633;17274:6107.boundVariables.topLeftRadius`; 80references. Aliases in YAML/snapshot.
- `stroke/xs` (VariableID:09bf0f399feb2dd1331a55f613f3fec11642c615/3639:793), FLOAT, REMOTE; sample `I15006:84201;17279:10633;17274:6107.boundVariables.strokeTopWeight`; 80references. Aliases in YAML/snapshot.
- `Color/text/brand` (VariableID:17569:27768), COLOR, LOCAL; sample `I15006:84201;17279:10633;17274:6107.boundVariables.strokes.0`; 60references. Aliases in YAML/snapshot.
- `icons/md-icon-size` (VariableID:476dc0c24aa3bd4a9d24e145c9b7f14063069900/4360:7), FLOAT, REMOTE; sample `I15006:84201;17279:10633;17274:6107;1430:18897.boundVariables.width`; 20references. Aliases in YAML/snapshot.
- `spacing/none` (VariableID:4f36a89ff3f1560665805305d5132f9b73d4b2ad/3639:849), FLOAT, REMOTE; sample `I15006:84201;17279:10633;17274:6107;1430:18898.boundVariables.itemSpacing`; 60references. Aliases in YAML/snapshot.
- `spacing/xs` (VariableID:90435138fcc3da9fb6d745fd768eea1072696e3e/3639:805), FLOAT, REMOTE; sample `I15006:84201;17279:10633;17274:6107;1430:18898.boundVariables.paddingLeft`; 250references. Aliases in YAML/snapshot.
- `radius/radius-full` (VariableID:c3b5a3b53e7cb477f0043af3d678d534ea99dcf4/4317:272), FLOAT, REMOTE; sample `I15006:84201;17279:10633;17274:6107;1430:18898.boundVariables.topLeftRadius`; 80references. Aliases in YAML/snapshot.
- `stroke/stroke-default` (VariableID:0caa4b020638062b7107a63deb45ff0893dd23c9/4331:1211), FLOAT, REMOTE; sample `I15006:84201;17279:10633;17274:6107;1430:18898.boundVariables.strokeTopWeight`; 80references. Aliases in YAML/snapshot.
- `color/feedback/danger/icon` (VariableID:9b1e68d1f4dd4f9560cbe322415f543969f12fdf/6075:39), COLOR, REMOTE; sample `I15006:84201;17279:10633;17274:6107;1430:18898.boundVariables.fills.0`; 40references. Aliases in YAML/snapshot.
- `color/border/on-brand` (VariableID:ec51ea7981e9079db3a1c4ec443ecfab50c11122/5638:36), COLOR, REMOTE; sample `I15006:84201;17279:10633;17274:6107;1430:18898.boundVariables.strokes.0`; 40references. Aliases in YAML/snapshot.
- `color/text/on-brand` (VariableID:21c68664aad258aad360610ceb69cc12c98be563/3639:900), COLOR, REMOTE; sample `I15006:84201;17279:10633;17274:6107;1430:18898;1133:31555.boundVariables.fills.0`; 40references. Aliases in YAML/snapshot.
- `font/weight/bold` (VariableID:68953aef437f5350d545fc4a9000b6ca1328f7b2/4655:15), STRING, REMOTE; sample `I15006:84201;17279:10633;17274:6107;1430:18898;1133:31555.boundVariables.fontStyle.0`; 20references. Aliases in YAML/snapshot.
- `font/family/base` (VariableID:5b6478e0ce1305efedeaf4a605843e3af57a32ca/3639:856), STRING, REMOTE; sample `I15006:84201;17279:10633;17279:5887;1133:31555.boundVariables.fontFamily.0`; 80references. Aliases in YAML/snapshot.
- `radius/sm` (VariableID:3ae4611e96f2ce2dea9afff292184554b70766d0/3639:798), FLOAT, REMOTE; sample `I15006:84201;15006:83003;15006:84568;17141:22308.boundVariables.topLeftRadius`; 280references. Aliases in YAML/snapshot.
- `color/feedback/positive/bg` (VariableID:43fe59b2dbaa0a2b3d6598e9420f6e428321b6d3/6075:96), COLOR, REMOTE; sample `I15006:84201;15006:83003;15006:84568;17141:22308.boundVariables.fills.0`; 140references. Aliases in YAML/snapshot.
- `color/feedback/positive/icon` (VariableID:bac769da2aa4520a8708f10d024390d0c88246b7/7596:2), COLOR, REMOTE; sample `I15006:84201;15006:83003;15006:84568;17141:22308;1234:66895;8899:27923.boundVariables.fills.0`; 140references. Aliases in YAML/snapshot.
- `color/feedback/positive/text` (VariableID:d28ce5904b5f1be08faf4711ad89f1de57815998/6075:76), COLOR, REMOTE; sample `I15006:84201;15006:83003;15006:84568;17141:22308;1234:65359.boundVariables.fills.0`; 280references. Aliases in YAML/snapshot.
- `font/letter-spacing/normal` (VariableID:79fe3a30a9b92bac34cd254ab77fd25797247666/3639:879), FLOAT, REMOTE; sample `I15006:84201;15006:83003;15006:84568;17141:22308;1234:65359.boundVariables.letterSpacing.0`; 70references. Aliases in YAML/snapshot.
- `font/size/xs` (VariableID:44a21f9f8d118524aceb4bab4db4c656140a3b4a/3639:861), FLOAT, REMOTE; sample `I15006:84201;15006:83003;15006:84568;17141:22308;1234:65359.boundVariables.fontSize.0`; 70references. Aliases in YAML/snapshot.
- `font/weight/regular` (VariableID:d9723f3635e7a39d3366f43f0c4fcbb13cfb1dea/4655:3), STRING, REMOTE; sample `I15006:84201;15006:83003;15006:84568;17141:22308;1234:65359.boundVariables.fontStyle.0`; 70references. Aliases in YAML/snapshot.
- `font/line-height/xs` (VariableID:5a156743257bea0783f4d33628bd3a8262bc35e2/3639:870), FLOAT, REMOTE; sample `I15006:84201;15006:83003;15006:84568;17141:22308;1234:65359.boundVariables.lineHeight.0`; 70references. Aliases in YAML/snapshot.

## 11. Content

Ten rows×seven columns are demonstration content. Full strings in inventory JSON and YAML; no tax/data-validation rule inferred.

## 12. Interactions

FIGMA_DEFINED: ON_HOVER from15006:83463 to19227:37531; no transition. Actions/sorting/selection semantics require product definition.

## 13. Accessibility

REQUIRES_DEFINITION: keyboard, names, sort announcements and full-value access for truncated text. No WCAG claim.

## 14. External Dependencies

Referenced icons, controls, badges and logo: active mains resolved. Library names/versions NOT_EXPOSED_BY_FIGMA_MCP.

## 15. Unresolved Information

TABLE-SOURCE-001: Row widens8px and first cell shrinks24px to insert24px action with8px gap. Column alignment shifts.

TABLE-SOURCE-002: Preferred keys differ from active definitions. Destination must map actual local keys; source remains unchanged.

TABLE-SOURCE-003: Usage paths sampled, full per-instance override arrays not archived. Partial metadata, not complete dependency contracts.

## 16. Implementation Notes

No product behavior inferred.

Ten rows and seven columns are observed sample counts, not cardinality rules.

Raw layout/paint snapshots supplement normalized summaries; no production code.

## 17. Evidence / Confidence

Observed from Figma: identity, geometry, bindings, source cells/containers and screenshot. Derived structure: grouping/counts. Requires definition: product semantics. Coverage1449/1449nodes including360locally hidden;456instances,15keys,36variable refs,2styles. Dependency metadata PARTIAL: sampled usage paths and no full overrides. See YAML model and linked snapshots; no Figma modifications in extraction.

